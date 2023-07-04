import csv
import json

csv_file = r"C:\Users\siranjeevi\Dropbox\PC\Downloads\Assignment\Assignment\county-info.csv"
json_file = "county-info.json"

data = []

# Read the CSV file and convert the data into a list of dictionaries
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Write the data to a JSON file
with open(json_file, 'w') as file:
    json.dump(data, file, indent=4)

print("Data converted to JSON and saved in 'county-info.json' file.")
