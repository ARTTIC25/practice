import pickle
import streamlit as st

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
  recommendation_list=[]
  for index,movie_data in enumerate(movie_list,start=1):
    movie_index=movie_data[0]
    similarity_score=round(movie_data[1]*100,2)
    title=movies.iloc[movie_index].title
    #print(f"{index}. {title} -> {similarity_score}% match")
    recommendation_list.append(title)
  return recommendation_list

st.title("Recommendation System\n")
movie=st.text_input("Enter the movie name :")

if st.button("recommend"):
  recommendations=recommend(movie)

for i in recommendations:
  st.write(i)