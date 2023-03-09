import requests
from bs4 import BeautifulSoup

BILLBOARD="https://www.billboard.com/charts/hot-100/"

# date_music=input("Date you want the list for (YYYY-MM-DD)")
# print(BILLBOARD + date_music)
url = BILLBOARD + "2008-03-10"

response = requests.get(url)
website_html = response.text

# print(website_html)

soup = BeautifulSoup(website_html, "html.parser")
first_song = soup.find_all(name="h3", class_="u-letter-spacing-0028@tablet")
first_song = first_song[0].getText().strip()

all_songs = soup.find_all(name="h3", class_="lrv-u-font-size-18@tablet")
all_songs_names = [first_song] + [song.getText().strip() for song in all_songs]
print(all_songs_names)


# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
#
# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         scope="playlist-modify-private",
#         redirect_uri="http://example.com",
#         client_id="9ccbac35f4434c6e9637d8b424eb7335",
#         client_secret="7d4e108c279d4d62bd306979ee5b519f",
#         show_dialog=True,
#         cache_path="token.txt"
#     )
# )
# user_id = sp.current_user()["id"]