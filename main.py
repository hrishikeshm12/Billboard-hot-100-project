import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

UNIQUE_CLIENT_ID=""
UNIQUE_CLIENT_SECRET=""
date=input("what year you would like to travel to in YYY-MM-DD format : ")


URL = f"https://www.billboard.com/charts/hot-100/{date}"

year=date.split('-')[0]


response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
top_100_songs_scraped = soup.select("li ul li h3")
top_100_songs=[]
for song in top_100_songs_scraped:
    name=song.getText().strip()
    top_100_songs.append(name)
# print(top_100_songs)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=UNIQUE_CLIENT_ID,
        client_secret=UNIQUE_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
top_100_songs_uri=[]
for track_name in top_100_songs:
    results = sp.search(q=f'track:{track_name} year:{year}', type='track', limit=1)
    if results['tracks']['items']:
        # Get the first track from the search results
        track = results['tracks']['items'][0]

        # Extract the Spotify URI
        spotify_uri = track['uri']
        top_100_songs_uri.append(spotify_uri)
    else:
        print("Track not found")
        spotify_uri = None

print(top_100_songs_uri)

#create a new playlist

new_playlist=sp.user_playlist_create(user=user_id,name=f"{date} Billboard 100",public=False, description=" A playlist of Top Billboard songs of a year")
print(new_playlist)
sp.playlist_add_items(playlist_id=new_playlist["id"],items=top_100_songs_uri)