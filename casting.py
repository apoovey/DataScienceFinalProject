import pandas as pd
import ast
import re

movies = pd.read_csv("data/data_cleaned.csv")
cast1 = pd.read_csv("raw_data/credits.csv")
cast2 = pd.read_csv("raw_data/AllMoviesCastingRaw.csv", sep=";")

d2 = cast2["director_name"]
d2_g = cast2["director_gender"]
id2 = cast2["id"]
a1 = cast2["actor1_name"]
a1_g = cast2["actor1_gender"]
a2 = cast2["actor2_name"]
a2_g = cast2["actor2_gender"]
a3 = cast2["actor3_name"]
a3_g = cast2["actor3_gender"]
a4 = cast2["actor4_name"]
a4_g = cast2["actor4_gender"]
a5 = cast2["actor5_name"]
a5_g = cast2["actor5_gender"]

cast = cast1["cast"]
crew = cast1["crew"]
id1 = cast1["id"]

actor1 = []
actor1_gender = []
actor2 = []
actor2_gender = []
actor3 = []
actor3_gender = []
director = []
director_gender = []

id = movies["id"]
company = movies["production_companies"]

y1 = 0
y2 = 0

#parse
for x in range (0, len(id)):
    if company[x].startswith("["):
        e = 0
        while id[x] != id1[y1]:
            y1 = y1 + 1
        d = ast.literal_eval(crew[y1])
        for y in range(0, len(d)):
            if "job" in d[y]:
                if d[y]["job"] == "Director":
                    director.append(d[y]["name"])
                    director_gender.append(d[y]["gender"])
                    e = 1
                    break
        if e == 0:
            director.append(None)
            director_gender.append(None)
        c = ast.literal_eval(cast[y1])
        if len(c) > 0:
            c1 = c[0]
            actor1.append(c1["name"])
            actor1_gender.append(c1["gender"])
        else:
            actor1.append(None)
            actor1_gender.append(None)
        if len(c) > 1:
            c2 = c[1]
            actor2.append(c2["name"])
            actor2_gender.append(c2["gender"])
        else:
            actor2.append(None)
            actor2_gender.append(None)
        if len(c) > 2:
            c3 = c[2]
            actor3.append(c3["name"])
            actor3_gender.append(c3["gender"])
        else:
            actor3.append(None)
            actor3_gender.append(None)
    else:
        while id[x] != id2[y2]:
            y2 = y2 + 1
        director.append(d2[y2])
        director_gender.append(d2_g[y2])
        if a1[y2] != "none":
            actor1.append(a1[y2])
            actor1_gender.append(a1_g[y2])
            actor2.append(a2[y2])
            actor2_gender.append(a2_g[y2])
            actor3.append(a3[y2])
            actor3_gender.append(a3_g[y2])
        elif a2[y2] != "none":
            actor1.append(a2[y2])
            actor1_gender.append(a2_g[y2])
            actor2.append(a3[y2])
            actor2_gender.append(a3_g[y2])
            actor3.append(a4[y2])
            actor3_gender.append(a4_g[y2])
        else:
            actor1.append(a3[y2])
            actor1_gender.append(a3_g[y2])
            actor2.append(a4[y2])
            actor2_gender.append(a4_g[y2])
            actor3.append(a5[y2])
            actor3_gender.append(a5_g[y2])



#pull data
print(director)
print(director_gender)
print(actor1)
print(actor1_gender)
print(actor2)
print(actor2_gender)
print(actor3)
print(actor3_gender)
print(len(director))
print(len(director_gender))
print(len(actor1))
print(len(actor1_gender))
print(len(actor2))
print(len(actor2_gender))
print(len(actor3))
print(len(actor3_gender))

cc = pd.DataFrame({"director":director,"director_gender":director_gender,"actor1":actor1,"actor1_gender":actor1_gender,
                   "actor2":actor2,"actor2_gender":actor2_gender,"actor3":actor3,"actor3_gender":actor3_gender})
cc = cc[["director","director_gender","actor1","actor1_gender","actor2","actor2_gender","actor3","actor3_gender"]]
cc.to_csv("data/cast_and_crew.csv")