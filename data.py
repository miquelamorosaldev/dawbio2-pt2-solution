import os
from urllib.request import urlretrieve
import pandas as pd

filepath = "hearth-attack-prediction.csv"

if not os.path.isfile(filepath):
    url = "https://gitlab.com/xtec/bio-data/-/raw/main/heart-attack-prediction.csv"
    urlretrieve(url, filepath)

df = pd.read_csv(filepath)
# print(df.iloc[0])

"""
data = df[df["Age"] == 30]
data = data.to_json(orient="records")
print(data)
"""