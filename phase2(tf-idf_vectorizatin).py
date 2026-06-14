import pandas as pd
#step1
from sklearn.feature_extraction.text import CountVectorizer
#step2
movies=pd.DataFrame({

  "movie":[
    "Batman Begins",
        "The Dark Knight",
        "Toy Story"],
  "tag":[ "action crime drama",
        "action crime drama",
        "animation comedy"]
})

cv=CountVectorizer()
vectors=cv.fit_transform(movies["tag"])
print(vectors.toarray())