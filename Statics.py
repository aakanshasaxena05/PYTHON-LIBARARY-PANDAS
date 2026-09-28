import pandas as pd

data = pd.DataFrame({
    "Name": ["Aakansha", "Rahul", "Priya", "Rohan", "Neha"],
    "Age": [21, 19, 22, 20, 19],
    "Marks": [75, 90, 65, 88, 95]
})

print(data)
# Average
print(data["Marks"].mean())

# Median
print(data["Marks"].median())

# Mode
print(data["Marks"].mode()[0])

# Minimum
print(data["Marks"].min())

# Maximum
print(data["Marks"].max())

# Standard deviation
print(data["Marks"].std())

# Number of values
print(data["Marks"].count())

# Variance
print(data["Marks"].var())

# Sum
print(data["Marks"].sum())