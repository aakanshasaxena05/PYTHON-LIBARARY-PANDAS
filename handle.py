# Handle missing values

import pandas as pd

# Read the Excel file
data = pd.read_excel(r"C:\Users\Lenovo\Downloads\dirty_insurance_dataset.xlsx")

# Display the complete dataset
print(data)

# Check the number of missing values in each column
print(data.isnull().sum())


# ------------------------------------------------
# Drop rows containing missing values
# ------------------------------------------------

# data.dropna(axis=0, inplace=True)

# Check missing values after removing rows
# print(data.isnull().sum())


# ------------------------------------------------
# Interpolation: estimating missing values
# using nearby available values
# ------------------------------------------------


# Polynomial interpolation for age
# Convert age into numeric datatype
# Invalid values are converted into NaN

data["age"] = pd.to_numeric(data["age"], errors="coerce")

# Fill missing age values using polynomial interpolation
# order=2 means a quadratic polynomial is used

data["age"] = data["age"].interpolate(method="polynomial", order=2)

# Display age column
print(data["age"])


# ------------------------------------------------
# Spline interpolation for charges
# ------------------------------------------------

# Convert charges into numeric datatype
# Invalid values are converted into NaN

data["charges"] = pd.to_numeric(data["charges"], errors="coerce")

# Fill missing charges using spline interpolation
# order=3 means a cubic spline is used

data["charges"] = data["charges"].interpolate(method="spline", order=3)

# Display charges column
print(data["charges"])


# ------------------------------------------------
# Backward Fill (bfill)
# ------------------------------------------------

# Fill missing sex values using the next available value

data["sex"] = data["sex"].bfill()


# ------------------------------------------------
# Forward Fill (ffill)
# ------------------------------------------------

# Fill missing children values using the previous available value

data["children"] = data["children"].ffill()


# ------------------------------------------------
# Fill missing smoker values
# ------------------------------------------------

# smoker is a categorical column (yes/no)
# Therefore, interpolation is not suitable
# bfill() fills missing values using the next available value

data["smoker"] = data["smoker"].bfill()


# ------------------------------------------------
# Fill missing region values
# ------------------------------------------------

# Replace missing region values with "southeast"

data["region"] = data["region"].fillna("southeast")


# ------------------------------------------------
# Check missing values after handling them
# ------------------------------------------------

print(data.isnull().sum())