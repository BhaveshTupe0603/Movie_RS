from flask import Flask, render_template, request, jsonify
from recommender import recommend_single, recommend_profile


app = Flask(__name__)




@app.route("/")

def home():
    return render_template("index.html")

@app.route("/api/recommend")
def recommend():
    title = request.args.get("title", "")
    min_votes = int(request.args.get("min_votes", 0))
    return jsonify(recommend_single(title, min_votes=min_votes))

@app.route("/api/profile", methods=["POST"])
def profile():
    data = request.get_json()
    titles = data.get("titles", [])
    min_votes = int(data.get("min_votes", 0))
    return jsonify(recommend_profile(titles, min_votes=min_votes))

if __name__ == "__main__":
    app.run(debug=True)
