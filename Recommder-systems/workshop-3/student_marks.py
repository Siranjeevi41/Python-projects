"""
Collaborative Filtering

"""

import pandas as pd
from surprise import Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import KNNBasic

# Example collaborative filtering dataset
marks_data = {
    'student_id': [1, 2, 3, 4, 5],
    'math': [90, 78, 95, 85, 88],
    'physics': [85, 92, 88, 90, 85],
    'chemistry': [88, 95, 80, 92, 78],
    'computer_science': [92, 88, 94, 78, 90],
    'radiology': [78, 85, 75, 80, 92]
}

marks_df = pd.DataFrame(marks_data)

# Save the dataset to a CSV file
marks_df.to_csv('marks_data.csv', index=False)

# Load the data using surprise
reader = Reader(line_format='user item rating', sep=',', rating_scale=(0, 100))
data = Dataset.load_from_df(marks_df.melt(id_vars='student_id', var_name='subject', value_name='rating'),
                            reader)

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
