import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Rahul", "Priya", "Neha", "Karan"],
    "Department": ["IT", "HR", "IT", "HR", "Sales", "IT"],
    "Marks": [90, 60, 90, 60, 65, 65],
    "Salary": [50000, 40000, 60000, 45000, 55000, 52000]
}

df = pd.DataFrame(data)

print(df)
r=df.groupby("Department")["Marks"].mean()
print(r)
m=df.groupby("Department")["Marks"].max()
print(m)
j=df.groupby("Marks")["Salary"].max()
print(j)