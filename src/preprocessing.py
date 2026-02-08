import os
import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def stem(text):
    return " ".join(ps.stem(word) for word in text.split())

def load_and_process_data():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    movies_path = os.path.join(BASE_DIR, "data", "raw", "tmdb_5000_movies.csv")
    credits_path = os.path.join(BASE_DIR, "data", "raw", "tmdb_5000_credits.csv")

    movies = pd.read_csv(movies_path)
    credits = pd.read_csv(credits_path)

    movies = movies.merge(credits, on="title")

    # keep only required columns
    movies = movies[["movie_id", "title", "overview", "genres",
                      "keywords", "cast", "crew"]]

    # helper functions
    def convert(text):
        return [i["name"] for i in ast.literal_eval(text)]

    def convert_cast(text):
        return [i["name"] for i in ast.literal_eval(text)[:3]]

    def fetch_director(text):
        for i in ast.literal_eval(text):
            if i["job"] == "Director":
                return [i["name"]]
        return []

    # apply transformations
    movies["genres"] = movies["genres"].apply(convert)
    movies["keywords"] = movies["keywords"].apply(convert)
    movies["cast"] = movies["cast"].apply(convert_cast)
    movies["crew"] = movies["crew"].apply(fetch_director)

    movies["overview"] = movies["overview"].fillna("").apply(lambda x: x.split())

    movies["tags"] = (
        movies["overview"]
        + movies["genres"]
        + movies["keywords"]
        + movies["cast"]
        + movies["crew"]
    )

    movies["tags"] = movies["tags"].apply(lambda x: " ".join(x))
    movies["tags"] = movies["tags"].apply(stem)

    # vectorization
    cv = CountVectorizer(max_features=5000, stop_words="english")
    vectors = cv.fit_transform(movies["tags"]).toarray()

    similarity = cosine_similarity(vectors)

    return movies, similarity



