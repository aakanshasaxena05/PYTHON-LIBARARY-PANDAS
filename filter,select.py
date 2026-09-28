import pandas as pd

# Read file
df = pd.read_excel(r"C:\Users\Lenovo\Downloads\Student_Data_100_Students.xlsx")
print(df.info())
#selecting one column
print(df["Semester"])
#slect 2 columns
print(df[["Student ID","Student Name"]])
#filtering one condition
print(df[df["Age"]>18])
#filtering using 2 condition
print(df[(df["Age"]>19) & (df["Marks"]>25)])
print(df)
print("MARKS ABOVE 65 in betch")
print(df[(df["Marks"]>65) & (df["Course"]=="B.Tech")])
print("either city is udaipur or alwar")
print(df[(df["City"]=="Udaipur")| (df["City"]=="Lucknow")])