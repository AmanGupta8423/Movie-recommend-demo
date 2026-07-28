# Movie Recommender System

A content-based movie recommendation web app built with Streamlit. Select any movie and get 5 similar movie recommendations along with their posters, computed using content-based similarity on a Kaggle movie dataset.

Live app: https://movie-recommend-aman-gupta.onrender.com/

Repository: https://github.com/AmanGupta8423/Movie-recommend-demo

---

## How to Use

1. Open the live app link above
2. Choose a movie from the dropdown search box
3. Click Recommend
4. View 5 similar movies with their posters

---

## Features

- Content-based movie recommendations using a precomputed similarity matrix
- Dropdown search across the full movie dataset
- Movie posters fetched live from The Movie Database (TMDB) API
- Returns top 5 most similar movies for any selected title

---

## Tech Stack

- Python
- Streamlit (web app UI)
- Pandas (data handling)
- Scikit-learn (similarity computation, used during model building)
- TMDB API (movie poster fetching)
- Dataset: Kaggle movie dataset
- Deployed on Render

---

## How It Works

1. Movie metadata and tags were preprocessed and vectorized from the Kaggle dataset
2. A cosine similarity matrix was precomputed across all movies based on content features (genre, cast, crew, keywords, overview)
3. The trained similarity matrix and movie index are loaded at runtime (large similarity file is hosted on Google Drive and downloaded on app startup)
4. When a user selects a movie, the app looks up its similarity scores against all other movies and returns the top 5 closest matches
5. Posters for the recommended movies are fetched live from the TMDB API

---

## Running Locally

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`
4. On first run, the app will automatically download the similarity matrix file

---

## Project Structure

```
Movie-recommend-demo/
├── app.py                # Streamlit app - UI, recommendation logic, poster fetching
├── movie_dict2.pkl       # Preprocessed movie metadata (titles, IDs)
├── requirements.txt      # Python dependencies
└── README.md
```

---

## License

Feel free to use or extend this project with attribution.

## About Me

Hi, I'm Aman Gupta — a Data Science Enthusiast and student at NIT Jamshedpur. I built this project to work hands-on with content-based recommendation systems and deploying ML-backed apps.

Connect with me:
LinkedIn: https://www.linkedin.com/in/aman-gupta-bb196621b/
GitHub: https://github.com/AmanGupta8423
Email: 2024ugpi049@nitjsr.ac.in
