import pandas as pd
import ast
import pickle

from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies=pd.read_csv("tmdb_5000_movies.csv")
credits=pd.read_csv("tmdb_5000_credits.csv")
ps=PorterStemmer()

#print(movies.columns)
#print(movies.head())
#print(credits.head())
#rint(movies.shape)
#print(credits.shape)

def recommend(movie):
  match_movie=movies[movies["title"].str.lower().str.contains(movie)]

  if match_movie.empty:
    print("no matching movie")
    return
  movie_index=match_movie.index[0]
  distance=list(enumerate(similarity[movie_index]))

  movie_list=sorted(distance,reverse=True,key=lambda x:x[1])[1:6]
  print("\nTop Recommendation:\n")
  for i in movie_list:
    print(movies.iloc[i[0]].title)
  
def stem(text):
  result=[]
  for i in text.split():
    result.append(ps.stem(i))
  return " ".join(result)

def convert(text):
  result=[]
  for i in ast.literal_eval(text):
    result.append(i["name"])
  return result

def convert2(text):
  result=[]
  counter=0
  for i in  ast.literal_eval(text):
    if counter!=3:
      result.append(i["name"])
      counter+=1
    else:
      break
  return result

def convert3(text):
  result=[]
  for i in ast.literal_eval(text):
    if i["job"]=="Director":
      result.append(i["name"])
  return result

def space(text):
  result=[]
  for i in text:
    result.append(i.replace(" ",""))
  return result

movies=movies.merge(credits,on="title")
movies=movies[[
   "movie_id",
    "title",
    "overview",
    "genres",
    "keywords",
    "cast",
    "crew"
]]
#print(movies.head())
movies.dropna(inplace=True)
#print(movies.isnull().sum())

movies["overview"]=movies["overview"].apply(lambda x:x.split())
#print(movies["overview"])

movies["genres"]=movies["genres"].apply(convert)
#print(movies.iloc[0].genres)

movies["keywords"]=movies["keywords"].apply(convert)
#print(movies.iloc[0].keywords)

movies["cast"]=movies["cast"].apply(convert2)
#print(movies["cast"].head())

movies["crew"]=movies["crew"].apply(convert3)
#print(movies["crew"].head())

movies["genres"]=movies["genres"].apply(space)
#print(movies.iloc[0].genres)

movies["keywords"]=movies["keywords"].apply(space)
#print(movies.iloc[0].keywords)

movies["cast"]=movies["cast"].apply(space)
#print(movies["cast"].head())

movies["crew"]=movies["crew"].apply(space)
#print(movies["crew"].head())

movies["tag"]=movies["overview"]+movies["genres"]+movies["cast"]+movies["crew"]+movies["keywords"]
movies["tag"]=movies["tag"].apply(lambda x:" ".join(x))
#print(movies["tag"].head())

movies["tag"]=movies["tag"].str.lower()
movies["tag"]=movies["tag"].apply(stem)
#print(movies["tag"][0])

cv=CountVectorizer(max_features=5000,stop_words="english")
vectors=cv.fit_transform(movies["tag"]).toarray()
#print(vectors.shape)

similarity=cosine_similarity(vectors)
#print(similarity.shape)

movie=input("Enter the movie name:").lower()
recommend(movie)

pickle.dump(movies,open("movies.pkl","wb"))
pickle.dump(similarity,open("similarity.pkl","wb"))
