import random
import sqlite3
import sys

from fuzzywuzzy import process
from matplotlib import pyplot as plt

from terminal_styles import *

# SQLite database name
DB_NAME = "movies.db"


def initialize_db():
    """
    Create a table in the database if it does not exist.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            rate REAL,
            year INTEGER
        )
    """)
    conn.commit()
    conn.close()


def get_all_movies():
    """
    Get all movies from the database.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT name, rate FROM movies")
    movies = dict(cursor.fetchall())
    conn.close()
    return movies


def add_movie():
    """
    Adds a new movie name and rating to the database if it doesn't already exist.
    It checks if the entered rating is in range 0 to 10.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    movies = get_all_movies()
    try:
        new_movie_name = input(input_announcements_msgs_with_blue_background("Enter new movie name: ")).title()
        if len(new_movie_name) > 0:
            if not new_movie_name in movies:
                new_movie_rating = float(input(input_announcements_msgs_with_blue_background(f"Enter new movie rating (1-10): ")))
                if 1 <= new_movie_rating <= 10:
                    cursor.execute("INSERT INTO movies (name, rate) VALUES (?, ?)", (new_movie_name, new_movie_rating))
                    print_green_background_success_message(f"Movie {new_movie_name} successfully added")
                else:
                    print_red_color_alert_with_black_background("Out of range!")
            else:
                print_red_color_alert_with_black_background(f"Movie {new_movie_name} already exists!")
        else:
            print_red_color_alert_with_black_background("You entered nothing!")
    except ValueError:
        print_red_color_alert_with_black_background("Invalid input!")
    except KeyboardInterrupt:
        print()
        print_announcements_msgs_with_yellow_background("Goodbye!")
        exit()
    conn.commit()
    conn.close()


def update_movie():
    """
    Updates a movie's rating if it exists.
    Ask the user for the new rating and checks if it's in range of 1 to 10.
    Then writes updated dictionary to database.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    movies = get_all_movies()
    try:
        movie_to_update = input(input_announcements_msgs_with_blue_background("Enter movie name: ")).title()
        if movie_to_update in movies:
            new_rate_to_update = float(input(input_announcements_msgs_with_blue_background("Enter new movie rating (0-10): ")))
            if 0 < new_rate_to_update <= 10:
                cursor.execute("UPDATE movies SET rate = ? WHERE name = ?", (new_rate_to_update, movie_to_update))
                print_green_background_success_message(f"Movie {movie_to_update} successfully updated")
            else:
                print_red_color_alert_with_black_background("Out of range!")
        else:
            print_red_color_alert_with_black_background(f"Movie {movie_to_update} doesn't exist!")
    except ValueError:
        print_red_color_alert_with_black_background("Invalid input!")
    except KeyboardInterrupt:
        print()
        print_announcements_msgs_with_yellow_background("Goodbye!")
        exit()
    conn.commit()
    conn.close()


def delete_movie():
    """
    Menu number 3.
    Deletes a movie of the user's choice from the database, if it exists.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        movie_to_delete = input(input_announcements_msgs_with_blue_background("Enter movie name to delete: ")).title()
        cursor.execute("DELETE FROM movies WHERE name = ?", (movie_to_delete,))
        if cursor.rowcount > 0:
            print_green_background_success_message(f"Movie {movie_to_delete} successfully deleted")
        else:
            print_red_color_alert_with_black_background(f"Movie {movie_to_delete} doesn't exist!")
    except KeyboardInterrupt:
        print()
        print_announcements_msgs_with_yellow_background("Goodbye!")
        exit()
    conn.commit()
    conn.close()


def show_all_movies():
    """
    Menu number 1.
    Shows all available movies and their ratings without sorting In a numbered list.
    """
    movies_dict = get_all_movies()
    print_announcements_with_blue_background(f"{len(movies_dict)} movies in total: ")
    for i, (name, rate) in enumerate(movies_dict.items(),1):
        print_result_with_green_background(f"{i}- {name} : {rate}")


def show_statistics():
    """
    Provides and shows a summary report of the movies, including:
    1- Average rating from all of movies
    2- Median rating in movies dict
    3- The best and worst movie
    """
    movies = get_all_movies()
    ratings = list(movies.values())
    average_rate = sum(ratings) / len(ratings)
    sorted_ratings = sorted(ratings)
    middle = len(ratings) // 2
    if len(sorted_ratings) % 2 != 0:
        median_rating = sorted_ratings[middle]
    else:
        median_rating =(sorted_ratings[middle - 1] + sorted_ratings[middle]) / 2
    best_movie = max(movies, key=movies.get)
    worst_movie = min(movies, key=movies.get)

    print_announcements_with_blue_background("Statistics: ")
    print_result_with_green_background(f"Average rating: {average_rate:.1f}")
    print_result_with_green_background(f"Median rating: {median_rating:.1f}")
    print_result_with_green_background(f"Best movie: {best_movie}, {movies[best_movie]}")
    print_result_with_green_background(f"Worst movie: {worst_movie}, {movies[worst_movie]}")


def random_movie():
    """
    Prints a random movie with its rating.
    """
    movies = get_all_movies()
    movie, rating = random.choice(list(movies.items()))
    print_result_with_green_background(f"Your movie for tonight: {movie}, it's rated {rating}")


def print_search_result(matched_name, partial_matched_names, searched_name):
    """
    If any movie matches, it prints the matched name as final search result,
    """
    if matched_name :
        print_announcements_msgs_with_yellow_background("Exact match found!")
        print_result_with_green_background(f"{matched_name}")
    elif partial_matched_names:
        print_red_color_alert_with_black_background(f"The movie {searched_name} not found!")
        print_announcements_msgs_with_yellow_background("Do you mean: ")
        for i, movie in enumerate(partial_matched_names):
            print_announcements_msgs_with_green_background_(f"{i + 1}- {movie}")
    else:
        print_red_color_alert_with_black_background(f"No results found for '{searched_name}'")


def search_movie():
    """
    Search for movies using fuzzywuzzy modul (fuzzy matching)
    """
    search_target_str = input(input_announcements_msgs_with_blue_background("Enter part of movie name: ")).lower()
    if len(search_target_str) > 0:
        movies =get_all_movies()
        movie_names_list = list(movies.keys())

        ratios = process.extract(search_target_str, movie_names_list)
        highest = process.extractOne(search_target_str, movie_names_list)

        matched_movie = ""
        partial_matched_movies = []

        for each_ratio in ratios:
            if 92 <= each_ratio[1] <= 100:
                matched_movie = highest[0]
            elif 80 <= each_ratio[1] < 92:
                partial_matched_movies.append(each_ratio[0])

        print_search_result(matched_movie, partial_matched_movies, search_target_str)
    else:
        print_red_color_alert_with_black_background("You entered nothing!")


def build_histogram():
    """"
    It uses matplotlib modul for drawing a downloadable histogram.
    """
    movies = get_all_movies()
    movies_rating_list = movies.values()
    plt.hist(movies_rating_list, bins=10)
    plt.show()


def sort_movies():
    """
    Sort movies by rating in descending order and display to the user.
    """
    movies = get_all_movies()
    sorted_movies_descending = dict(sorted(movies.items(), key=lambda item: item[1], reverse=True))
    print_announcements_with_blue_background("Sorted by rating: ")
    for movie,rate in sorted_movies_descending.items():
        print_result_with_green_background(f"{movie}: {rate}")


def menu():
    """
    Displays the menu and asks the user to select a number from the menu.

    """
    bye = lambda: (print("Bye!") or sys.exit())
    options = {
        0: ("Exit", bye),
        1: ("List movies", show_all_movies),
        2: ("Add movie", add_movie),
        3: ("Delete movie", delete_movie),
        4: ("Update movie", update_movie),
        5: ("Stats", show_statistics),
        6: ("Random movie", random_movie),
        7: ("Search movie", search_movie),
        8: ("Movies sorted by rating", sort_movies),
        9: ("Create Rating Histogram", build_histogram)
    }

    while True:
        print_announcements_with_blue_background("Menu:")
        for key, (desc, _) in options.items():
            print_result_with_green_background(f"{key}. {desc}")

        try:
            print_emoji_chars_with_yellow_background("🎥🍿🎬🍿🎥")
            choice = int(input(input_announcements_msgs_with_yellow_background("Select from the menu (1-9): ")))
            print_emoji_chars_with_yellow_background("🎥🍿🎬🍿🎥")
            if choice in options:
                options[choice][1]()
                print_emoji_chars_with_yellow_background("😎🍿🎥🎉🎬")
                input(input_announcements_msgs_with_blue_background(f"Press enter to continue: "))
                print_emoji_chars_with_yellow_background('🎥🍿🎬🍿🎥')

            else:
                print_red_color_alert_with_black_background("Invalid option!")

        except ValueError:
            print_red_color_alert_with_black_background("Invalid input!")
        except KeyboardInterrupt:
            print()
            print_announcements_msgs_with_yellow_background("Goodbye!")
            break

def show_top_main_header():
    """
    It prints main top header in two rows, first row Title and second row imojis.
    """
    print(
        "********************************************* My Movies Database *********************************************\n")


def main():
    """
    It starts the program with calling the initialization database function and menu function.
    Also shows the top header once.
    """
    show_top_main_header()
    initialize_db()
    menu()


if __name__ == "__main__":
    main()
