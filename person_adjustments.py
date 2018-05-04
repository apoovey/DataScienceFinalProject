import pandas as pd
import operator

movies = pd.read_csv("data/data_prod_cleaned.csv")

#creating dictionaries
dict = {}
for n in range(1980,2018):
    dict[n] = {}
    year = pd.read_csv("data/years/" + str(n))
    for x in range(0,len(year['actor'])):
        dict[n][year['actor'][x]] = year['star_power'][x]
    print n
    print dict[n]

dirW = {}
dirN = {}
dirs = pd.read_csv("raw_data/220k_awards_by_directors.csv")
names = dirs["director_name"]
out = dirs["outcome"]
for n in range(0, len(names)):
    name = names[n]
    if out[n] == "Won":
        if name in dirW:
            dirW[name] = dirW[name] + 1
        else:
            dirW[name] = 1
    if name in dirN:
        dirN[name] = dirN[name] + 1
    else:
        dirN[name] = 1
print dirW
print dirN

prodM = {}
prodD = {}
prods = pd.read_csv("data/high_prods.csv")
p_names = prods["prod_company"]
p_movies = prods["num_movies"]
p_bo = prods["dom_box_office"]
for n in range(0, len(p_names)):
    name = p_names[n]
    if (p_names[n] == "Disney-Pixar"):
        name = "Pixar Animation Studios"
    if (p_names[n] == "Twentieth Century Fox"):
        name = "Twentieth Century Fox Film Corporation"
    if (p_names[n] == "Metro-Goldwyn-Mayer Pictures"):
        name = "Metro-Goldwyn-Mayer (MGM)"
    if (p_names[n] == "Tri-Star Pictures"):
        name = "TriStar Pictures"
    prodM[name] = p_movies[n]
    prodD[name] = p_bo[n]

print prodM
print prodD

do = pd.read_csv("raw_data/Yearly_box_office.csv")

gpm = {}
year = do["Year"]
gross = do["Total Gross*"]
movie = do["# of Movies"]

for x in range(0,len(year)):
    gros = float(gross[x].replace("$","").replace(",",""))*1000000
    gpm[year[x]] = (gros/movie[x])

print gpm
######################

star_power = []
years = movies["year"]
actor1 = movies["actor1"]
actor2 = movies["actor2"]
actor3 = movies["actor3"]
for n in range(0,len(years)):
    p = 0
    year = years[n] - 1
    if year in dict:
        if actor1[n] in dict[year]:
            p = p + dict[year][actor1[n]]
        else:
            p = p
        if actor2[n] in dict[year]:
            p = p + dict[year][actor2[n]]
        else:
            p = p
        if actor3[n] in dict[year]:
            p = p + dict[year][actor3[n]]
        else:
            p = p
        star_power.append(p)
    else:
        star_power.append(0)

print(star_power)

wins = []
noms = []
directors = movies["director"]
for n in range(0,len(directors)):
    d = directors[n]
    if d in dirW:
        wins.append(dirW[d])
    else:
        wins.append(0)
    if d in dirN:
        noms.append(dirN[d])
    else:
        noms.append(0)
print wins
print noms

prod_bo = []
prod_bop = []
cos = movies["prod_company"]
for n in range(0,len(cos)):
    co = cos[n]
    if co in prodD:
        prod_bo.append(prodD[co])
        prod_bop.append(prodD[co]/prodM[co])
    else:
        prod_bo.append(0)
        prod_bop.append(0)
print prod_bo
print prod_bop

ygpm = []
years = movies["year"]
for n in range(0,len(years)):
    year = years[n] - 1
    if year in gpm:
        ygpm.append(gpm[year])
    else:
        ygpm.append(0)


new_cols = pd.DataFrame({"star_power":star_power,"director_wins":wins,"director_noms":noms,"prod_company_dom_box_office":prod_bo,"prod_company_dom_box_office_per_movie":prod_bop,"prev_yr_gross_per_movie":ygpm})
act = {}
actor1.fillna(0)
actor2.fillna(0)
actor3.fillna(0)
for n in range(0,len(actor1)):
    a1 = actor1[n]
    a2 = actor2[n]
    a3 = actor3[n]
    if a1 != 0 and a1 != 'none':
        if a1 in act:
            act[a1] = act[a1] + 1
        else:
            act[a1] = 1
    if a2 != 0 and a2 != 'none':
        if a2 in act:
            act[a2] = act[a2] + 1
        else:
            act[a2] = 1
    if a3 != 0 and a3 != 'none':
        if a3 in act:
            act[a3] = act[a3] + 1
        else:
            act[a3] = 1
print(sorted(act.items(),key=operator.itemgetter(1), reverse=True))

movies = pd.get_dummies(movies, columns=["director_gender","actor1_gender","actor2_gender","actor3_gender"])
movies = movies.drop(["Unnamed: 0", "Unnamed: 0.1", "Unnamed: 0.1.1", "director_gender_0.0", "actor1_gender_0.0",
                      "actor2_gender_0.0", "actor3_gender_0.0"], axis=1)
for x in list(new_cols):
    movies[x] = new_cols[x]
print movies
print(list(movies))

num = 0
n2 = 0
n3 = 0
b = 0
for x in range(0,len(years)):
    if years[x] < 1981:
        num = num + 1
    if movies["prev_yr_gross_per_movie"][x] == 0:
        n2 = n2 + 1
    if movies["star_power"][x] == 0:
        n3 = n3 + 1
    if movies["adjusted_budget"][x] == 0:
        b = b + 1
print num
print n2
print n3
print b

movies.to_csv("data/data_rec.csv")