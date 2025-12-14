let profile = [];

async function search() {
  const title = movie.value;
  const minVotes = votes.value;

  const res = await fetch(
    `/api/recommend?title=${encodeURIComponent(title)}&min_votes=${minVotes}`
  );
  render(await res.json());
}

// ---------------- PROFILE LOGIC ----------------

function addProfile() {
  const input = document.getElementById("profileInput");
  const movie = input.value.trim();

  if (!movie) return;

  if (!profile.includes(movie)) {
    profile.push(movie);
  }

  input.value = "";
  renderProfile();
}

function removeProfile(movie) {
  profile = profile.filter(m => m !== movie);
  renderProfile();
}

async function profileRecommend() {
  if (profile.length === 0) {
    alert("Add at least one movie to profile");
    return;
  }

  const res = await fetch("/api/profile", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      titles: profile,
      min_votes: votes.value
    })
  });

  render(await res.json());
}

function renderProfile() {
  const container = document.getElementById("profileList");
  container.innerHTML = "";

  profile.forEach(movie => {
    const div = document.createElement("div");
    div.className = "profile-item";

    div.innerHTML = `
      <span>${movie}</span>
      <button onclick="removeProfile('${movie}')">✖</button>
    `;

    container.appendChild(div);
  });
}

// ---------------- RESULTS ----------------

function render(data) {
  const results = document.getElementById("results");
  results.innerHTML = "";   // clear previous results

  data.forEach(m => {
    results.innerHTML += `
      <div class="card">
        <div class="poster-wrapper">
          ${
            m.poster
              ? `<img src="${m.poster}" alt="${m.title} poster">`
              : `<div class="no-poster">No Poster</div>`
          }
        </div>

        <h3>${m.title}</h3>
        <div class="meta">${m.genre}</div>
        <div class="meta">⭐ ${m.rating} | ${m.votes}</div>
        <p>${m.overview}</p>
      </div>
    `;
  });
}
