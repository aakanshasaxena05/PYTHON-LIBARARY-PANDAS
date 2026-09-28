import pandas as pd
import numpy as np

# Create a DataFrame
data = pd.DataFrame({
    "Name": ["Aakansha", "Rahul", "Priya", "Rohan", "Neha"],
    "Age": [20, np.nan, 22, 21, np.nan],
    "Marks": [85, 90, np.nan, 75, 80],
    "City": ["Jaipur", np.nan, "Delhi", "Jaipur", np.nan]
})

print(data)

# Check missing values
print(data.isnull().sum())


# -----------------------------------------
# 1. Fill with a FIXED VALUE
# -----------------------------------------

# Replace missing City values with "Jaipur"

data["City"] = data["City"].fillna("Jaipur")


# -----------------------------------------
# 2. Fill with MEAN
# -----------------------------------------

# Replace missing Age values with the average age

data["Age"] = data["Age"].fillna(data["Age"].mean())


# -----------------------------------------
# 3. Fill with MEDIAN
# -----------------------------------------

# Replace missing Marks with the median marks

data["Marks"] = data["Marks"].fillna(data["Marks"].median())


# -----------------------------------------
# 4. Fill with MODE
# -----------------------------------------

# Find the most frequently occurring city

# data["City"] = data["City"].fillna(data["City"].mode()[0])


# -----------------------------------------
# 5. Forward Fill (ffill)
# -----------------------------------------

# Missing value gets the previous available value

data["Age"] = data["Age"].ffill()


# -----------------------------------------
# 6. Backward Fill (bfill)
# -----------------------------------------

# Missing value gets the next available value

data["Marks"] = data["Marks"].bfill()


# -----------------------------------------
# Check missing values
# -----------------------------------------

print(data)

print(data.isnull().sum())