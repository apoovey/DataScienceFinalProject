import pandas as pd
data = pd.read_csv("MovieTableBoxOffice.csv")
print(len(data))
for index, row in data.iterrows():
    print(row)