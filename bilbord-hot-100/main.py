from bs4 import BeautifulSoup
import requests
import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# to install with success use python-dotenv in settings/project day-x/pythoninterpreter
load_dotenv()

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

date = input("Input the date from when you want to "
             "receive Billboard Hot 100 songs. "
             "Use this format: YYYY-MM-DD ")
# date = "2000-08-12"
year = date.split("-")[0]


# Scrapping hot 100 titles form billboard
url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url=url, headers=header)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
# print(song_names)

song_authors_spans = soup.select("li ul li span")
song_authors = [author.getText().strip() for author in song_authors_spans]
artists = song_authors[0::7]
# print(artists)


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ["YOUR_APP_CLIENT_ID"],
                                               client_secret=os.environ["YOUR_APP_CLIENT_SECRET"],
                                               redirect_uri=os.environ["YOUR_APP_REDIRECT_URI"],
                                               scope="playlist-modify-private",
                                               cache_path="token.txt"))

results = sp.current_user()
USER_ID = results['id']


# Searching Spotify for songs by title
uri_list = []
for n in range(0, len(song_names)):
    try:
        result = sp.search(q=f"track: {song_names[n]} year: {year} artist: {artists[n]}", type="track")
        uri_list.append(result['tracks']['items'][0]['uri'])
    except IndexError:
        print(f"{song_names[n]} doesn't exist in Spotify. Skipped.")
# print(uri_list)


# Creating a new private playlist in Spotify
PLAYLIST_ID = sp.user_playlist_create(USER_ID, public=False, name=f"{date} BillBoard-100")['id']

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=PLAYLIST_ID, items=uri_list)
