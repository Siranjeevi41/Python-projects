from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from sqlalchemy import create_engine
import pandas as pd

# Connect to your SQL database
engine = create_engine('sqlite:///your_database.db')

# Query data from the database
query = "SELECT * FROM your_table"
df = pd.read_sql(query, engine)

# Generate PDF
def generate_pdf(dataframe, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    
    # Set up the table headers
    headers = list(dataframe.columns)
    header_widths = [len(header) * 12 for header in headers]  # Adjust width based on header length
    data_widths = [max(len(str(val)) * 12, 50) for val in dataframe.values.flatten()]  # Minimum width
    
    # Determine column widths
    column_widths = [max(header_widths[i], data_widths[i]) for i in range(len(headers))]
    
    # Set up the table
    c.setFont("Helvetica-Bold", 10)
    y_start = 750
    for i, header in enumerate(headers):
        c.drawString(40 + sum(column_widths[:i]), y_start, header)
    
    c.line(40, y_start - 10, sum(column_widths) + 40, y_start - 10)
    
    # Add data to the table
    c.setFont("Helvetica", 10)
    for row_idx, row in dataframe.iterrows():
        y_start -= 20
        for col_idx, val in enumerate(row):
            c.drawString(40 + sum(column_widths[:col_idx]), y_start, str(val)[:100])  # Limit text length for display
    
    c.save()

# Generate PDF with the data
generate_pdf(df, "output.pdf")