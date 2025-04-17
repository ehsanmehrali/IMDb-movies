# 🎥 My Movies Database 🎬

A simple and colorful command-line application for managing your personal movie collection using SQLite. With features like fuzzy search, statistics, and matplotlib-based histograms, this tool makes it fun and efficient to track and explore your favorite movies.

---

## ✨ Features

- Add new movies with ratings (1–10)
- Update or delete existing movies
- View a list of all movies
- Sort movies by rating (descending)
- Fuzzy search for movie names (using fuzzywuzzy)
- Get a random movie suggestion
- View statistical insights:
  - Average rating
  - Median rating
  - Best and worst rated movies
- Visualize ratings using a histogram (via matplotlib)
- Stylish and colorful terminal output using ANSI escape codes

---

## 🏗️ Project Structure

```bash
IMDb-movieas
    │ 
    ├── main.py # Main application script # 
    ├── terminal_styles.py # Custom terminal styling functions 
    ├── movies.db # SQLite database (auto-created on first run) 
    ├── requirements.txt # List of required Python libraries 
    └── README.md # Project documentation
```
