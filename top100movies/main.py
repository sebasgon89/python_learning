import bs4
import requests
from bs4 import BeautifulSoup

MOVIES_URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(MOVIES_URL)
website_html = response.text

soup = bs4.BeautifulSoup(website_html, "html.parser")