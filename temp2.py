import pandas as pd
data = pd.read_csv("movies_metadata.csv")
data2 = pd.read_csv("AllMoviesDetailsCleaned.csv", sep=";")
sum = 0
movies = {}
df1 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
for index in range(0, len(data)):
    x = data['revenue'][index]
    # y = data['budget'][index]
    if x > 100000 and data['original_language'][index] == "en":
        sum += 1
        movies[data['original_title'][index]] = 1
print(sum)
for index in range(0, len(data2)):
    x = data2['revenue'][index]
    y = data2['budget'][index]
    if x > 100000 and data2['original_language'][index] == "en":
        sum += 1
        movies[data2['original_title'][index]] = 1


data3 = pd.read_csv("MovieData.csv")
for index in range(0, len(data3)):
    x = data3['production_budget'][index]
    y = data3['domestic_box_office'][index]
    if x != 0 and y > 100000:
        sum += 1
        movies[data3['movie_name'][index]] = 1

print(sum)
print(len(movies))
# movies.sort()
m = sorted(movies)
for n in m:
    print(n)
