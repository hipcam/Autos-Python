from django.shortcuts import render
import pandas as pd 
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(url, header = None)
df.head(5)
path="C:\Users\FERNANDA_ALEXIS\Downloads\automoviles.csv"
df.to_csv(path)
