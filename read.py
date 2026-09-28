import pandas as pd

# Read file
df = pd.read_excel(r"C:\Users\Lenovo\Downloads\clean_insurance_data.xlsx")

# Display complete data
print(df)

# Display first 5 rows
print(df.head())

# Display last 5 rows
print(df.tail())

# Display rows and columns
print(df.shape)

# Display column names
print(df.columns)

# Display data types
print(df.dtypes)

# Display information
print(df.info())

print(df.describe())