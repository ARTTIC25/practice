import pickle

movies=pickle.load(open("movies.pkl","rb"))
similarity=pickle.load(open("similarity.pkl","rb"))

def recommend(movie):
  match_movie=movies[movies["title"].str.lower().str.contains(movie)]

  if match_movie.empty:
    print("NO such movie found")
    return
  movie_index=match_movie.index[0]
  distance=list(enumerate(similarity[movie_index]))

  movie_list=sorted(distance,reverse=True,key=lambda x:x[1])[1:6]
  print("\nTop movie recommendation\n")
  for i in movie_list:
    print(movies.iloc[i[0]].title)

movie=input("Enter the movie name :").lower()
recommend(movie)