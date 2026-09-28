import streamlit as st
import pickle
import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity

st.title("🎬 Movie Recommender System")

@st.cache_resource
def load_data():
    movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    movies_df = pd.DataFrame(movie_dict)
    vectors_matrix = sparse.load_npz('vectors.npz')
    return movies_df, vectors_matrix

movies, vectors = load_data()

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    movie_vector = vectors[movie_index]
    similarity_scores = cosine_similarity(movie_vector, vectors).flatten()
    
    movie_indices = sorted(list(enumerate(similarity_scores)), reverse=True, key=lambda x: x[1])[1:6]
    recommendations = [movies.iloc[i[0]].title for i in movie_indices]
    return recommendations

selected_movie = st.selectbox("Select a movie:", movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.subheader("Top Recommendations:")
    for title in recommendations:
        st.write(f"- {title}")