import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommend_movies=[]
    for i in movies_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies
similarity=pickle.load(open('similarity.pkl','rb'))

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
st.title('SHREYAS RANGA MOVIE RECOMMENDATION')
option= st.selectbox(
'Enter movies for recommendation',movies['title'].values)
if st.button('RECOMMEND'):
     recommendations=recommend(option)
     for i in recommendations:
         st.write(i)
