# Collaborative Filtering

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Example content-based filtering dataset
content_data = {
    'course_id': [1, 2, 3, 4, 5],
    'content': [
        "Introduction to Python programming for beginners.",
        "Intermediate-level course on machine learning fundamentals.",
        "Advanced web development with Django framework.",
        "Intermediate-level data science course using Python.",
        "Free course on JavaScript for beginners."
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

# Get recommendations for a specific course
course_index = 0  # Index of the course you want recommendations for
similar_courses = list(enumerate(cosine_sim[course_index]))

# Print the similar courses
for course in similar_courses:
    print(course)
