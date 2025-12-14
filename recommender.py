import os
import pickle
import numpy as np
import pandas as pd
import scipy.sparse as sp
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Load poster CSV
poster_df = pd.read_csv("movie_posters.csv")

# Create lookup dictionary
poster_map = {
    row["Movie_Title"].strip().lower(): row["Poster_URL"]
    for _, row in poster_df.iterrows()
}

BASE = os.path.dirname(__file__)
ART = os.path.join(BASE, "recommender_artifacts")

tfidf = pickle.load(open(os.path.join(ART, "tfidf_vectorizer.pkl"), "rb"))
tfidf_matrix = sp.load_npz(os.path.join(ART, "tfidf_matrix.npz"))
df = pd.read_csv(os.path.join(ART, "movies_parsed.csv"))
df["Movie_Title"] = df["Movie_Title"].astype(str)

indices = pd.Series(df.index, index=df["Movie_Title"]).to_dict()

def recommend_single(title, topn=10, min_votes=0):
    if title in indices:
        idx = indices[title]
    else:
        match = df[df["Movie_Title"].str.lower().str.contains(title.lower())]
        if match.empty:
            return []
        idx = match.index[0]

    sim = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
    scores = sorted(enumerate(sim), key=lambda x: x[1], reverse=True)

    return _build(scores, [idx], topn, min_votes)

def recommend_profile(titles, topn=10, min_votes=0):
    liked = []
    for t in titles:
        if t in indices:
            liked.append(indices[t])
        else:
            match = df[df["Movie_Title"].str.lower().str.contains(t.lower())]
            if not match.empty:
                liked.append(match.index[0])

    if not liked:
        return []

    sims = cosine_similarity(tfidf_matrix[liked], tfidf_matrix)
    avg_sim = np.mean(sims, axis=0)
    scores = sorted(enumerate(avg_sim), key=lambda x: x[1], reverse=True)

    return _build(scores, liked, topn, min_votes)
def _build(scores, exclude, topn, min_votes):
    out = []

    for i, s in scores:
        if i in exclude:
            continue

        if df.loc[i, "Movie_Vote_Count"] < min_votes:
            continue

        title = df.loc[i, "Movie_Title"]

        poster = poster_map.get(title.lower())

        out.append({
            "title": title,
            "genre": df.loc[i, "Movie_Genre"],
            "rating": df.loc[i, "Movie_Vote"],
            "votes": int(df.loc[i, "Movie_Vote_Count"]),
            "overview": df.loc[i, "Movie_Overview"][:300],
            "poster": poster
        })

        if len(out) == topn:
            break

    return out
