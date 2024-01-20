import pandas as pd
from surprise import Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import KNNBasic

# Example collaborative filtering dataset
courses_data = {
    'course_id': [1, 2, 3, 4, 5],
    'course_name': ['Introduction to Python', 'Machine Learning Fundamentals', 'Web Development with Django',
                    'Data Science with Python', 'JavaScript for Beginners'],
    'category': ['Programming', 'Machine Learning', 'Web Development', 'Data Science', 'Programming'],
    'level': ['Beginner', 'Intermediate', 'Advanced', 'Intermediate', 'Beginner'],
    'price': ['Free', 29.99, 49.99, 39.99, 'Free'],
    'rating': [4.5, 4.0, 4.8, 4.2, 4.0]
}

courses_df = pd.DataFrame(courses_data)

# Save the dataset to a CSV file
courses_df.to_csv('courses_data.csv', index=False)

# Load the data using surprise
reader = Reader(line_format='user item rating', sep=',', rating_scale=(0, 5))
data = Dataset.load_from_df(courses_df[['course_id', 'course_name', 'rating']], reader)

# Split data into training and testing sets
trainset, testset = train_test_split(data, test_size=0.25)

# Build and train the model
sim_options = {'name': 'cosine', 'user_based': False}
model = KNNBasic(sim_options=sim_options)
model.fit(trainset)

# Make predictions
predictions = model.test(testset)

# Print the predictions
for prediction in predictions:
    print(prediction)
