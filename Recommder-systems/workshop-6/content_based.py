import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Example content-based filtering dataset
content_data = {
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami'],
    'content': [
        "Mild temperature, moderate humidity, and moderate wind speed.",
        "High temperature, low humidity, and low wind speed.",
        "Cool temperature, high humidity, and high wind speed.",
        "Hot temperature, high humidity, and moderate wind speed.",
        "Hot temperature, high humidity, and low wind speed."
    ]
}

content_df = pd.DataFrame(content_data)

# Save the dataset to a CSV file
content_df.to_csv('content_data.csv', index=False)

# Load the content data
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(content_df['content'])

# Compute the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Get recommendations for a specific city
city_index = 0  # Index of the city you want recommendations for
similar_cities = list(enumerate(cosine_sim[city_index]))

# Print the similar cities
for city in similar_cities:
    print(city)
