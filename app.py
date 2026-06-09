import os
import gdown

FILE_ID = "1Jmj-72FgzgKN0A7AXCER38n35jlbRoeB"

if not os.path.exists("similarity.pkl"):
    gdown.download(
        id=FILE_ID,
        output="similarity.pkl",
        fuzzy=True
    )
    
import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict = pickle.load(open('movie_dict2.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse = True , key = lambda x:x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api tmdb
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=4662847884411f835d7f6b838488a311&language=en-US"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            print("TMDB Error:", response.status_code)
            return "https://via.placeholder.com/500x750?text=No+Poster"

        data = response.json()

        if data.get('poster_path'):
            return "https://image.tmdb.org/t/p/w500" + data['poster_path']

        return "https://via.placeholder.com/500x750?text=No+Poster"

    except Exception as e:
        print("Connection Error:", e)
        return "https://via.placeholder.com/500x750?text=No+Poster"

st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
"Choose the movie",
movies['title'].values
)


if st.button("Recommend"):
    names,poster = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(poster[0])

    with col2:
        st.text(names[1])
        st.image(poster[1])

    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])
