import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Example content-based filtering dataset
content_data = {
    'item_id': [101, 102, 103, 104],
    'content': [
        "This is the content for item 101.",
        "Content for item 102 is different.",
        "Item 103 has unique content.",
        "Content of item 104 is interesting."
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

# Get recommendations for a specific item
item_index = 0  # Index of the item you want recommendations for
similar_items = list(enumerate(cosine_sim[item_index]))

# Print the similar items
for item in similar_items:
    print(item)