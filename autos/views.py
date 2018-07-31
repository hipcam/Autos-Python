from django.shortcuts import render
import pandas as pd 
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(url, header = None)
print("Done")
# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
headers
df.columns = headers
df.head(10)
df.dropna(subset=["price"], axis=0)
path=r"C:\Users\FERNANDA_ALEXIS\Downloads\automoviles.csv"
df.to_csv(path)
