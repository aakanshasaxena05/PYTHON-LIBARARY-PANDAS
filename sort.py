import pandas as pd

# Create DataFrame
data = pd.DataFrame({
    "Name": ["Aakansha", "Rahul", "Priya", "Rohan", "Neha", "Karan"],
    "Age": [21, 19, 22, 20, 19, 21],
    "Marks": [75, 90, 65, 88, 95, 70],
    "City": ["Jaipur", "Delhi", "Mumbai", "Jaipur", "Delhi", "Mumbai"]
})

print(data)
#2 columns sort
data.sort_values(["Age","Marks"],inplace=True)
print(data)
#descending
data.sort_values("Age",inplace=True,ascending=False)
print(data)
#ascending
data.sort_values("Marks",inplace=True)
print(data)