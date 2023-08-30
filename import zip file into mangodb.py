import zipfile
import json
from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["product_database"]
collection = db["products"]

# Path to the uploaded zip file
zip_path = "C:\\Users\\siranjeevi\\Dropbox\\PC\\Downloads\\productsList.zip"

# Extract and import products from the zip file into MongoDB
with zipfile.ZipFile(zip_path, "r") as zip_ref:
    for file_name in zip_ref.namelist():
        with zip_ref.open(file_name) as product_file:
            product_data = product_file.read()
            # Assuming product data is in JSON format
            product_json = product_data.decode("utf-8")
            
            # Parse JSON string into a dictionary
            product_dict = json.loads(product_json)

            # Insert the product data into MongoDB
            collection.insert_one(product_dict)
            
print("Products imported successfully.")
