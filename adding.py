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

print(df)
df["Average"]=df["Marks"]/800
print(df)
#insert at specific column
df.insert(1,"remark",[1,2,3,4,5,6,7,8])
print(df)
#updating row
df.loc[0,"Age"]=19
print(df)