import requests
import pandas as pd

x = []
for i in range (1,50,2):
    response = requests.get("https://hacker-news.firebaseio.com/v0/item/" + str(i*3000) + ".json")
    x.append(response.json())

df = pd.io.json.json_normalize(x)
print(df.shape)
print(df.columns)

df.to_csv("hn.csv")
