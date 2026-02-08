import streamlit as st
from src.preprocessing import load_and_process_data
from src.recommender import recommend

import streamlit as st


from src.preprocessing import load_and_process_data


@st.cache_data
def load_data():
    return load_and_process_data()

movies, similarity = load_data()


st.set_page_config(page_title="Movie Recommender", layout="wide")

st.title("🎬 Movie Recommendation System")

with st.spinner("Loading data..."):
    movies, similarity = load_and_process_data()

movie_name = st.selectbox("Select a movie", movies["title"].values)

if st.button("Recommend"):
    recommendations = recommend(movie_name, movies, similarity)

    st.subheader("Recommended Movies")
    for movie in recommendations:
        st.write(movie)
