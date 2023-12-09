from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

url = 'https://theresanaiforthat.com/saved/'

# Set up Chrome options to run headless (without opening a visible browser window)
chrome_options = Options()
chrome_options.add_argument('--headless')

# Initialize the Selenium WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open the URL
driver.get(url)

# Wait for dynamic content to load (adjust the sleep duration if needed)
time.sleep(5)

# Get the page source after dynamic content is loaded
page_source = driver.page_source

# Parse the HTML content of the page
soup = BeautifulSoup(page_source, 'html.parser')

# Find the element containing the recommended AIs based on saves
recommended_ais = soup.find('div', class_='based-on-saves')

if recommended_ais:
    # Extract AI names
    ai_names = [ai.text.strip() for ai in recommended_ais.find_all('div', class_='ai-name')]

    # Extract number of saves for each AI (assuming it's in the same structure)
    saves_counts = [int(count.text.strip()) for count in recommended_ais.find_all('span', class_='save-count')]

    # Create a list of tuples containing AI names and their saves counts
    ai_data = list(zip(ai_names, saves_counts))

    # Sort the AI data based on saves counts in descending order
    sorted_ai_data = sorted(ai_data, key=lambda x: x[1], reverse=True)

    # Print the sorted AI data
    for ai_name, saves_count in sorted_ai_data:
        print(f'{ai_name}: {saves_count} saves')
else:
    print('No recommended AIs based on saves found on the page.')

# Close the browser window
driver.quit()
