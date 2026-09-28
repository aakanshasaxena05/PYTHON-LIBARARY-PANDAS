import pandas as pd
d={"name":["a","b"],"age":[10,20],"city":["jaipur","delhi"]}
data=pd.DataFrame(d)
print(data)
data.to_csv("output.csv")