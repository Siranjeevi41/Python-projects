from pymongo import MongoClient
from datetime import datetime

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["product_database"]
collection = db["products"]

# 2. Find all products produced in the same country
print("2. Products produced in the same country:")
same_country_products = collection.aggregate([
    {"$group": {"_id": "$production_country", "products": {"$push": "$product_name"}}},
    {"$match": {"$expr": {"$gt": [{"$size": "$products"}, 1]}}}
])
for result in same_country_products:
    print(result)

# 3. Find all products with sales greater than 2500
print("\n3. Products with sales greater than 2500:")
high_sales_products = collection.find({"sales": {"$gt": 2500}})
for product in high_sales_products:
    print(product)

# 4. Find all products produced in the same city
print("\n4. Products produced in the same city:")
same_city_products = collection.aggregate([
    {"$group": {"_id": "$production_city", "products": {"$push": "$product_name"}}},
    {"$match": {"$expr": {"$gt": [{"$size": "$products"}, 1]}}}
])
for result in same_city_products:
    print(result)

# 5. Find all products produced in the same country (again)
print("\n5. Products produced in the same country:")
same_country_products = collection.aggregate([
    {"$group": {"_id": "$production_country", "products": {"$push": "$product_name"}}},
    {"$match": {"$expr": {"$gt": [{"$size": "$products"}, 1]}}}
])
for result in same_country_products:
    print(result)

# 6. Find all products produced in more than one country
print("\n6. Products produced in more than one country:")
multi_country_products = collection.aggregate([
    {"$group": {"_id": "$product_name", "countries": {"$addToSet": "$production_country"}}},
    {"$match": {"$expr": {"$gt": [{"$size": "$countries"}, 1]}}}
])
for result in multi_country_products:
    print(result)

# 7. Find all products produced in the same country (once again)
print("\n7. Products produced in the same country:")
same_country_products = collection.aggregate([
    {"$group": {"_id": "$production_country", "products": {"$push": "$product_name"}}},
    {"$match": {"$expr": {"$gt": [{"$size": "$products"}, 1]}}}
])
for result in same_country_products:
    print(result)

# 8. Find all products sold on 2022-01-03
print("\n8. Products sold on 2022-01-03:")
sales_date = datetime(2022, 1, 3)
print("Querying for date:", sales_date)
specific_date_products = collection.find({"sales_date": sales_date})
for product in specific_date_products:
    print(product)
