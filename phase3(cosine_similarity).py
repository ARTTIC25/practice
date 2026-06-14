import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend(movie_name):
  matching=movies[movies["title_lower"].str.contains(movie_name)]
  if matching.empty:
    print("no movie found")
    return
  movie_index=matching.index[0]
  distance=list(enumerate(similarity[movie_index]))
  distance=sorted(distance,reverse=True,key=lambda x:x[1])
  found=False
  for movie in distance[1:6]:#prints top 5 
  
    if (movie[1]>0):
     found=True
     print(movies.iloc[movie[0]].title,"->",round(movie[1],2)*100,"%")
  if not found:
    print("no similar movies")

movies=pd.read_csv("tmdb_5000_movies.csv")
credits=pd.read_csv("tmdb_5000_credits.csv")
print(movies.columns)
print(credits.columns)
print(movies.head())
print(credits.head())
print(movies.shape)
print(credits.shape)


#movies["title_lower"]=movies["title"].str.lower()
#movies["genre"]=movies["genre"].str.lower()
#movies["genre"]=movies["genre"].str.replace("|"," ",regex=False)

cv=CountVectorizer()
vectors=cv.fit_transform(movies["genre"])

similarity=cosine_similarity(vectors)

#movie_name=input("Enter the exact movie name:").lower()
#recommend(movie_name)