document.addEventListener("DOMContentLoaded", () => {
  const INTRO_DURATION = 4500; // must match animation timing

  setTimeout(() => {
    const intro = document.getElementById("container");
    const app = document.getElementById("app");

    // Remove intro
    if (intro) {
      intro.remove();
    }

    // Show app
    if (app) {
      app.classList.remove("hidden");
    }

    // Restore scrolling
    document.body.classList.remove("intro-active");
  }, INTRO_DURATION);
});
