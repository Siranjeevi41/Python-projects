from bs4 import BeautifulSoup
import requests
import csv

# Define the URLs for each mobile phone brand
urls = {
    '10.or Mobile Phones': 'https://www.gadgets360.com/mobiles/10-or-phones',
    'Acer Mobile Phones': 'https://www.gadgets360.com/mobiles/acer-phones',
    'Adcom Mobile Phones': 'https://www.gadgets360.com/mobiles/adcom-phones',
    'Airtel Mobile Phones': 'https://www.gadgets360.com/mobiles/airtel-phones',
    'Alcatel Mobile Phones': 'https://www.gadgets360.com/mobiles/alcatel-phones',
    'Alpha Mobile Phones': 'https://www.gadgets360.com/mobiles/alpha-phones',
    'Amazon Mobile Phones': 'https://www.gadgets360.com/mobiles/amazon-phones',
    'AOC Mobile Phones': 'https://www.gadgets360.com/mobiles/aoc-phones',
    'Apple Mobile Phones': 'https://www.gadgets360.com/mobiles/apple-phones',
    'Aqua Mobile Phones': 'https://www.gadgets360.com/mobiles/aqua-phones',
    'Archos Mobile Phones': 'https://www.gadgets360.com/mobiles/archos-phones',
    'Asus Mobile Phones': 'https://www.gadgets360.com/mobiles/asus-phones',
    'Benq Mobile Phones': 'https://www.gadgets360.com/mobiles/benq-phones',
    'Billion Mobile Phones': 'https://www.gadgets360.com/mobiles/billion-phones',
    'Black Shark Mobile Phones': 'https://www.gadgets360.com/mobiles/black-shark-phones',
    'BlackBerry Mobile Phones': 'https://www.gadgets360.com/mobiles/blackberry-phones',
    'Blu Mobile Phones': 'https://www.gadgets360.com/mobiles/blu-phones',
    'BQ Mobile Phones': 'https://www.gadgets360.com/mobiles/bq-phones',
    'Byond Mobile Phones': 'https://www.gadgets360.com/mobiles/byond-phones',
    'Cat Mobile Phones': 'https://www.gadgets360.com/mobiles/cat-phones'
}

# Iterate over each brand and scrape mobile phone models
for brand, url in urls.items():
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the container that holds the mobile phone models
        container = soup.find('div', class_='productList')

        if container:
            # Initialize a list to store the mobile phone models
            models = []

            # Find all list items within the container
            items = container.find_all('div', class_='productCard')

            # Extract the text from list items and add models to the list
            for item in items:
                model_name = item.find('div', class_='productCard__name').text.strip()
                models.append(model_name)

            # Write the models to a CSV file
            filename = f'{brand.replace(" ", "_")}_models.csv'
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Mobile Models'])
                writer.writerows([[model] for model in models])

            print(f'Scraped {len(models)} models for {brand}. Saved to {filename}')
        else:
            print(f'Container not found for {brand}. Please check the HTML structure.')

    except Exception as e:
        print(f'Error occurred for {brand}: {e}')
