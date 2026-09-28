import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Aarav", "Ananya", "Rahul", "Priya", "Rohan", "Neha", "Karan", "Ishita"],
    "Age": [20, 19, 21, 20, 22, 19, 21, 20],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
    "Course": ["BCA", "BCA", "BCA", "BCA", "BCA", "BCA", "BCA", "BCA"],
    "Marks": [85, 92, 68, 76, 55, 88, 72, 95],
    "Attendance": [90, 95, 78, 85, 70, 92, 80, 96]
}

df = pd.DataFrame(data)
#updating row
df.loc[0,"Age"]=19
print(df)
#updating column existing
df["Marks"]=df["Marks"]+12
print(df)
#removing
df.drop(columns=["Age"],inplace=True)
print(df)
