import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movies_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movies_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True,  key =lambda x:x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
       movie_id = movies.iloc[i[0]].movie_id 
       recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies = pickle.load(open('artifacts/movies.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))
movies_list = movies['title'].values
print(movies_list)

st.title('Movie Recommender System')
selected_movie = st.selectbox('Select a movie', movies_list)
if st.button('Recommend'):
    st.write('You selected:', selected_movie)
    recommendations = recommend(selected_movie)
    st.write('Recommended Movies:', recommendations)

    
    
    