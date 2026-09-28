import pandas as pd

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Aman', 'Riya', 'Rahul']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 4],
    'Marks': [85, 90, 78]
})
#outer merge
r=pd.merge(df1,df2,on="ID",how="outer")
print(r)
#inner merge
i=pd.merge(df1,df2,on="ID",how="inner")
print(i)
#left merge
l=pd.merge(df1,df2,on="ID",how="left")
print(l)
#right
l=pd.merge(df1,df2,on="ID",how="right")
print(l)


#join
import pandas as pd

df1 = pd.DataFrame({
    "Name": ["Aman", "Riya", "Rahul"]
}, index=[1, 2, 3])

df2 = pd.DataFrame({
    "Marks": [80, 70, 90]
}, index=[1, 2, 3])

result = df1.join(df2)

print(result)