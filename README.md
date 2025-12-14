# 🎬 Movie Recommendation System

A **content-based Movie Recommendation System** built using **Python, Flask, and Machine Learning**.  
The system recommends movies similar to a selected movie using **TF-IDF vectorization** and **cosine similarity**.

---

## 📌 Features

- Content-based movie recommendations
- TF-IDF + cosine similarity approach
- Clean and responsive UI
- Displays movie posters
- Fast recommendations using precomputed artifacts
- Flask-based web application

---

## 🧠 Tech Stack

- **Python**
- **Flask**
- **Scikit-learn**
- **Pandas**
- **NumPy**
- **HTML, CSS, JavaScript**

---

## 📂 Project Structure

```text
Movie_RS/
│
├── app.py
├── recommender.py
├── requirements.txt
├── movie_posters.csv
├── recommender_artifacts/
│   ├── movies_parsed.csv
│   ├── tfidf_matrix.npz
│   ├── tfidf_vectorizer.pkl
│   └── title_to_index.csv
│
├── static/
│   ├── style.css
│   ├── app.js
│   ├── no-poster.jpg
│   └── intro/
│       ├── intro.css
│       ├── intro.js
│       └── intro.sass
│
├── templates/
│   ├── index.html
│   └── intro/
│       └── intro.html
│
└── .gitignore
```
## How It Works

- Movie metadata is processed and vectorized using TF-IDF
- Cosine similarity is computed between movies
- On user selection, top similar movies are fetched
- Posters and titles are displayed on the web interface

---

## How to Run Locally

Clone the Repository

git clone https://github.com/BhaveshTupe0603/Movie_RS.git  
cd Movie_RS

Create Virtual Environment (Optional but Recommended)

python -m venv .venv  
source .venv/Scripts/activate

Install Dependencies

pip install -r requirements.txt

Run the Application

python app.py

Open in Browser

http://127.0.0.1:5000

---

## Dataset

- Movie metadata used for TF-IDF vectorization
- Poster data stored in movie_posters.csv
- Precomputed ML artifacts stored in recommender_artifacts/

---

## Future Enhancements

- Add collaborative filtering
- User login and history-based recommendations
- Deploy on cloud platforms such as Render, Railway, or Streamlit
- Improve UI animations
- Add genre-based filtering

---

## Author

Bhavesh Tupe  
GitHub: BhaveshTupe0603

---

## Support

If you like this project, give it a star on GitHub.

