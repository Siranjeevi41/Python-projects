from pymongo import MongoClient
import json

# Connection parameters
mongodb_url = "mongodb://localhost:27017/"  # Replace with your MongoDB connection URL
db_name = "village"
collection_name = "village"
json_file_path = "C:/Users/siranjeevi/Dropbox/PC/Downloads/village-details.json"

# Connect to MongoDB
client = MongoClient(mongodb_url)
db = client[db_name]
collection = db[collection_name]

# Load JSON data and insert into the collection
with open(json_file_path) as json_file:
    data = json.load(json_file)
    collection.insert_many(data)

print("Data imported successfully!")
