🎬 Movie Recommendation System

A content-based movie recommendation system built with Python and Streamlit using the TMDB 5000 dataset. It recommends movies based on similarity in genres, keywords, and cast.


Features

- Content-based recommendations using Cosine Similarity
- Interactive Streamlit web app for real-time recommendations
- Preprocessing pipeline for movie metadata: genres, keywords, cast
- Modular code structure for easy expansion (e.g., hybrid or deep learning models)


Tech Stack

- Python – data processing and logic
- Pandas & NumPy – data manipulation
- Scikit-Learn – Cosine Similarity calculation
- Streamlit – web interface for live recommendations

How to Use

1. Clone the repository:
git clone https://github.com/divya-sri18/movie-recommendation-system.git

2. Navigate to the project folder and activate your virtual environment:
cd movie-recommender
python -m venv venv
venv\Scripts\activate  # Windows

3. Install dependencies:
pip install -r requirements.txt

4. Run the Streamlit app:
streamlit run app.py

Dataset

- TMDB 5000 Movies and Credits datasets
- Preprocessed locally (not included in repo to reduce size)



