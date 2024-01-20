# Collaborative Filtering

import pandas as pd
from surprise import Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import KNNBasic

# Example collaborative filtering dataset
weather_data = {
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami'],
    'temperature': [75, 85, 65, 90, 88],
    'humidity': [60, 40, 70, 80, 75],
    'wind_speed': [10, 5, 15, 12, 8],
    'precipitation': [0.2, 0, 0.5, 0.1, 0.3],
    'cloudiness': [30, 10, 50, 20, 40]
}

weather_df = pd.DataFrame(weather_data)

# Save the dataset to a CSV file
weather_df.to_csv('weather_data.csv', index=False)

# Load the data using surprise
reader = Reader(line_format='user item rating', sep=',', rating_scale=(0, 100))
data = Dataset.load_from_df(weather_df.melt(id_vars='city', var_name='feature', value_name='rating'),
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
