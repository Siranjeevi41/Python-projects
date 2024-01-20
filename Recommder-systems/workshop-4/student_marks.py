# Content-Based Filtering

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Example content-based filtering dataset
content_data = {
    'student_id': [1, 2, 3, 4, 5],
    'content': [
        "High marks in Math, Physics, and Computer Science.",
        "Strong in Physics, Chemistry, and Radiology.",
        "Top performer in Math and Computer Science.",
        "Good in Physics, Chemistry, and Radiology.",
        "Well-rounded with good marks in all subjects."
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

# Get recommendations for a specific student
student_index = 0  # Index of the student you want recommendations for
similar_students = list(enumerate(cosine_sim[student_index]))

# Print the similar students
for student in similar_students:
    print(student)
