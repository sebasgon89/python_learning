import requests
from bs4 import BeautifulSoup

MOVIES_URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(MOVIES_URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

all_movie_titles = [movie.getText() for movie in all_movies]

movies = all_movie_titles[::-1]
# print(movies)

with open("movies.txt", mode="a", encoding="utf-8") as file:
    for movie in movies:
        # print(movie)
        file.write(f"{movie}\n")