import pandas as pd
from sqlalchemy import create_engine

# Replace 'your_password' with the actual password for the root user
db_url = "mysql+mysqlconnector://root:41465887@localhost:3306/demo"

# Create a SQLAlchemy engine
engine = create_engine(db_url)

# Specify the CSV file path
csv_file = r"C:\Users\siranjeevi\Dropbox\PC\Downloads\city_house_prices.csv"

# Read CSV into a DataFrame
df = pd.read_csv(csv_file)

# Specify the table name in MySQL
table_name = 'city_house_prices'

# Write the DataFrame to MySQL
df.to_sql(table_name, con=engine, if_exists='append', index=False)
