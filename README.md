# 🎬 Movie Recommender System

A content-based movie recommender system that suggests relevant movies based on user selection. Built using Python, Scikit-Learn, and deployed as an interactive web application with Streamlit.

🔗 **Live Application:** [https://movie-recommender-system00.streamlit.app/](https://movie-recommender-system00.streamlit.app/)

---

## 📌 Project Overview

This project implements a **Content-Based Filtering** recommendation engine using text data from approximately 5,000 movies in the TMDB dataset. The system extracts relevant metadata (genres, overview, keywords, top cast, and director), preprocesses and stems the text, converts it into feature vectors, and computes similarity scores using **Cosine Similarity**[cite: 1].

---

## 🚀 Features

- **Content-Based Filtering:** Recommends the top 5 most similar movies based on semantic and keyword overlap[cite: 1].
- **Lightweight Architecture:** Utilizes compressed sparse representations (`scipy.sparse`) for feature vectors to minimize storage and memory footprint.
- **On-the-Fly Similarity Scoring:** Calculates cosine similarity dynamically for the selected title to optimize compute time.
- **Interactive Web Interface:** Minimal and responsive user interface powered by Streamlit.

---

## 🛠️ Tech Stack & Libraries

- **Language:** Python
- **Data Manipulation:** Pandas, NumPy[cite: 1]
- **NLP & Feature Engineering:** NLTK (PorterStemmer), Scikit-Learn (CountVectorizer)[cite: 1]
- **Similarity Metric:** Cosine Similarity[cite: 1]
- **Web App Framework:** Streamlit
- **Deployment:** Streamlit Community Cloud

---

## ⚙️ How It Works

1. **Data Preprocessing:**
   - Merged the TMDB movies and credits datasets on `title`[cite: 1].
   - Filtered essential columns: `movie_id`, `title`, `overview`, `genres`, `keywords`, `cast`, and `crew`[cite: 1].
   - Extracted top 3 cast members and the primary director[cite: 1].
   - Cleaned spaces from multi-word tokens (e.g., `"James Cameron"` $\rightarrow$ `"JamesCameron"`) to avoid ambiguous vector weights[cite: 1].

2. **Feature Extraction:**
   - Concatenated overview, genres, keywords, cast, and director into a unified `tags` column[cite: 1].
   - Applied Porter Stemming to reduce words to their root forms (e.g., `loving`, `loved` $\rightarrow$ `love`)[cite: 1].
   - Generated a 5,000-dimensional bag-of-words matrix using `CountVectorizer` after removing English stop words[cite: 1].

3. **Recommendation Engine:**
   - Given a query movie, the engine extracts its feature vector and calculates the cosine distance against all other vectors[cite: 1].
   - Sorts the scores in descending order and returns the top 5 nearest neighbors[cite: 1].

---

## 📁 Repository Structure

```text
├── app.py                  # Streamlit application script
├── main.ipynb              # Exploratory Data Analysis, preprocessing & modeling notebook
├── movie_dict.pkl          # Serialized movie dictionary mapping titles and IDs
├── vectors.npz             # Compressed sparse matrix of text feature vectors
├── requirements.txt        # Required Python packages for deployment
└── README.md               # Project documentation
