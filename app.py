import pickle
import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY=os.getenv("API_KEY")

movies=pickle.load(open("movies.pkl","rb"))
similarity=pickle.load(open("similarity.pkl","rb"))

def fetch_poster(movie_id):
   url=f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
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
  similarity_score=[]
  recommended_movie=[]
  recommended_posters=[]
  #print("\nTop movie recommendation\n")
  
  for index,movie_data in movie_list:
    movie_id=movies.iloc[index].movie_id
    recommended_movie.append(movies.iloc[index].title)
    recommended_posters.append(fetch_poster(movie_id))
    similarity_score.append(round(movie_data*100,2))
  return recommended_movie,recommended_posters,similarity_score


st.title("Movie Recommendation System")

movie_list=movies["title"].values
selected_movie=st.selectbox("Select a movie",movie_list)


if st.button("Recommend"):
    with st.spinner("Finding your recommendation...."):
      name,poster,ss=recommend(selected_movie.lower())
      col1,col2,col3,col4,col5 =st.columns(5)
    
    with col1:
       st.text(name[0])
       st.text(f"{ss[0]}% Match")
       st.image(poster[0])

    with col2:
       st.text(name[1])
       st.text(f"{ss[1]}% Match")
       st.image(poster[1])

    with col3:
       st.text(name[2])
       st.text(f"{ss[2]}% Match")
       st.image(poster[2])
    
    with col4:
       st.text(name[3])
       st.text(f"{ss[3]}% Match")
       st.image(poster[3])

    with col5:
       st.text(name[4])
       st.text(f"{ss[4]}% Match")
       st.image(poster[4])
