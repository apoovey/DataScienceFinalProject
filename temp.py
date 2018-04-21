import pandas as pd
data = pd.read_csv("AllMoviesDetailsCleaned.csv", sep=";")
print(data.head(2))
print(data['budget'])
sum = 0
for num in data['budget']:
    if num == 0:
        sum += 1;
print(sum)
print(data['revenue'])
both = 0
for index in range(0, len(data['revenue'])):
    x = data['revenue'][index]
    y = data['budget'][index]
    if x != 0 and y != 0:
        both += 1
print(both)

