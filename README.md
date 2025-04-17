# 🎥 IMDb Movies Sample Database 🎬

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
    ├── main.py # Main application script # 
    ├── terminal_styles.py # Custom terminal styling functions 
    ├── movies.db # SQLite database (auto-created on first run) 
    ├── requirements.txt # List of required Python libraries 
    └── README.md # Project documentation
```

---

## 📦 Requirements

- Python 3.7 or higher
- Required libraries (install using pip):
```yaml
pip install -r requirements.txt
```
requirements.txt contents:

```nginx
fuzzywuzzy
python-Levenshtein
matplotlib
```

--- 

## 🚀 How to Run

1. Clone the repository or download the source files.
2. (Optional) Create and activate a virtual environment.
3. Install dependencies with pip.
4. Run the application:

```bash

python main.py
```

---

## 🖥️ Sample Output

```markdown
********************************************* My Movies Database *********************************************
                                                 🎥🍿🎬🍿🎥

Menu:
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
9. Create Rating Histogram

                                                 🎥🍿🎬🍿🎥
Select from the menu (1–9):
```

---

## 📊 Rating Histogram
Choosing option 9 displays a histogram of all movie ratings using matplotlib.

Note: Some servers or online IDEs may not support GUI rendering for plots.

---

## ⚠️ Notes

- The program uses ANSI escape codes for styling, so it looks best in modern terminals (e.g., Linux terminal, macOS Terminal, Windows Terminal).
- If you're running this in a limited or non-GUI environment, matplotlib’s plotting might not display.

---

## 👨‍💻 Developer

Built with ❤️ by ehsan mehrali  .

Feel free to customize, expand, or contribute!