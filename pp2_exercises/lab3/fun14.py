
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
def high_imdb(movie):
    for i in movies:
        if i["name"] == movie and i["imdb"] > 5.5:
            imdb1 = True 
        elif i["name"] == movie and i["imdb"] < 5.5:
            imdb1 = False
    return imdb1

def sublist(movies):
    sublist1=[]
    for j in movies:
        if j["imdb"] > 5.5:
            sublist1.append(j["name"])
    return sublist1
def one_category(movies, category1):
    sublist2=[]
    for x in movies:
        if x["category"]==category1:
            sublist2.append(x["name"])
    return sublist2
def average_imdb(movies):
    n=len(movies)
    sum=0
    for y in movies:
        sum+=y["imdb"]
    return sum/n
def average_imdb_category(movies,category2):
    sum2=0
    n2=0
    for z in movies:
        if z["category"]==category2:
            sum2+=z["imdb"]
            n2=n2+1
    return sum2/n2
            