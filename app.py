import pickle
import streamlit as st
import requests

movies=pickle.load(open("movies.pkl","rb"))
similarity=pickle.load(open("similarity.pkl","rb"))

def fetch_poster(movie_id):
   url=f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=6ad1c84f483ea69345147278898318d3&language=en-US"
   data=requests.get(url)
   data=data.json()
   
   poster_path= data["poster_path"]
   full_path="https://image.tmdb.org/t/p/w500/"+poster_path
   return  full_path

def recommend(movie):
  match_movie=movies[movies["title"].str.lower().str.contains(movie)]

  if match_movie.empty:
    #print("NO such movie found")
    return [],[]
  movie_index=match_movie.index[0]
  distance=list(enumerate(similarity[movie_index]))
  movie_list=sorted(distance,reverse=True,key=lambda x:x[1])[1:6]
  recommended_movie=[]
  recommended_posters=[]
  #print("\nTop movie recommendation\n")
  
  for i in movie_list:
    movie_id=movies.iloc[i[0]].movie_id
    recommended_movie.append(movies.iloc[i[0]].title)
    recommended_posters.append(fetch_poster(movie_id))
  return recommended_movie,recommended_posters


st.title("Movie Recommendation System")

movie_list=movies["title"].values
selected_movie=st.selectbox("Select a movie",movie_list)


if st.button("Recommend"):
    name,poster=recommend(selected_movie.lower())
    col1,col2,col3,col4,col5 =st.columns(5)
    
    with col1:
       st.text(name[0])
       st.image(poster[0])

    with col2:
       st.text(name[1])
       st.image(poster[1])

    with col3:
       st.text(name[2])
       st.image(poster[2])
    
    with col4:
       st.text(name[3])
       st.image(poster[3])

    with col5:
       st.text(name[4])
       st.image(poster[4])
