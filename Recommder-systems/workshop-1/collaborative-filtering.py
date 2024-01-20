import pandas as pd
from surprise import Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import KNNBasic

# Example collaborative filtering dataset
collab_data = {
    'user_id': [1, 1, 2, 2, 3, 3],
    'item_id': [101, 102, 101, 103, 102, 104],
    'rating': [5, 4, 3, 5, 2, 4]
}

collab_df = pd.DataFrame(collab_data)

# Save the dataset to a CSV file
collab_df.to_csv('collab_data.csv', index=False)

# Load the data using surprise
reader = Reader(line_format='user item rating', sep=',', rating_scale=(1, 5))
data = Dataset.load_from_df(collab_df[['user_id', 'item_id', 'rating']], reader)

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
    
"""
The message "Done computing similarity matrix" is specific to the KNNBasic collaborative filtering algorithm in the surprise library, and it might not be applicable to content-based filtering.

"""

