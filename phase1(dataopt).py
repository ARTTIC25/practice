import pandas as pd
#step1
movies=pd.DataFrame({
  "title":["Batman Begins",
        "Toy Story",
        "The Dark Knight",
        "Jumanji"],
  "genre":["Action|Crime|Drama",
        "Animation|Comedy",
        "Action|Crime|Drama",
        "Adventure|Fantasy"]
})
print(movies)

#step2
movies["genre"]=movies["genre"].str.lower()
print(movies)

#step3
movies["genre"]=movies["genre"].str.replace("|"," ",regex=False)
print(movies)

#step4
movies["tag"]=movies["title"]+" "+movies["genre"]
print(movies)