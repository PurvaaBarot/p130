import pandas as pd
df=pd.read_csv("merged_dataset.csv")
df=df.dropna()
del df["Luminosity"]
del df["temp_Star_name"]
del df["temp_Distance"]
del df["temp_Mass"]
del df["temp_Radius"]

df.to_csv("main.csv")