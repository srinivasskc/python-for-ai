import pandas as pd
import json
import os

# Check if we're in the right place
print("Current directory:", os.getcwd())

# Check if our data file exists
data_path = "data/sales.csv"
if os.path.exists(data_path):
    print(f"✅ Found {data_path}")
else:
    print(f"❌ Cannot find {data_path}")
    print("Make sure you're running from the sales-analysis folder!")

# -------------------------------

# Read the CSV file
df = pd.read_csv('data/sales.csv')
print("CSV Data:")
print(df)
print(df.shape)
print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns")

# Quick operation: calculate total for each row
df['total'] = df['quantity'] * df['price']
print("\nWith totals:")
print(df)

# Create output directory
os.makedirs('output', exist_ok=True)
# exist_ok=True: It’s fine if the directory exists. dont throw an error.

# Save as different formats
# 1. JSON format (good for web APIs)
# Converts df to Json file.
# orient="records", each row in dataframe becomes separate json object inside a list.

df.to_json('output/sales_data.json', orient='records', indent=2)

# 2. Excel format (good for sharing)
# To write to excel - pip install openpyxl
df.to_excel('output/sales_data.xlsx', index=False)


# 3. Updated CSV (with our new total column)
df.to_csv('output/sales_with_totals.csv', index=False)

# Convert to Txt.
df.to_csv('output/sales_with_totals.txt',sep=" ",index=False)



print("\nFiles saved:")
print("- output/sales_data.json")
print("- output/sales_data.xlsx") 
print("- output/sales_with_totals.csv")
print("- output/sales_with_totals.txt")


# Reading the Files.
# Read CSV File.

df_sales_csv = pd.read_csv("data/sales.csv")
print(df_sales_csv)

# Read CSV File with totals.

df_sales_total = pd.read_csv("output/sales_with_totals.csv")
print(df_sales_total)

# Read JSON File.
df_sales_json = pd.read_json("output/sales_data.json")
print(df_sales_json)

# Simple Json:
# opens json in read mode.
# json.load(file) - parses the json file to json object (list)
with open("output/sales_data.json","r") as file:
    data = json.load(file)
    print(data)
    print(type(data))

# Reads Excel File.
df_sales_excel = pd.read_excel("output/sales_data.xlsx")
print(df_sales_excel)

# Reads Text File.
with open("output/sales_with_totals.txt","r") as f:
    data = f.read()
    print(data)

    