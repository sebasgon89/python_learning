import requests
from bs4 import BeautifulSoup

BILLBOARD="https://www.billboard.com/charts/hot-100/"

date_music=input("Date you want the list for (YYYY-MM-DD)")
# print(BILLBOARD + date_music)
url = BILLBOARD + date_music

response = requests.get(url)
website_html = response.text

# print(website_html)

soup = BeautifulSoup(website_html, "html.parser")
all_songs = soup.find_all(name="h3", class_="a-no-trucate")
all_songs_names =[song.getText() for song in all_songs]
print(all_songs_names)

# Angela's solution again is not valid
# song_names_spans = soup.find_all("span", class_="chart-element__information__song")
# song_names = [song.getText() for song in song_names_spans]
# print(song_names)