"""
Scrape1 is the data scraping tool of Hamusic for Discz.
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config

client_credentials_manager = SpotifyClientCredentials(config.CLIENT_ID, config.CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# URL to playlist - can be replaced with any playlist
# currently using the top 500 songs of 2022
playlist_url = "https://open.spotify.com/playlist/4NdZwQEEKF3cTKnB30lti1"
uri = playlist_url.split("/")[-1].split("?")[0]

song_data = []

i = 0


for track in sp.playlist_tracks(uri, limit = 100)["items"]:
    song = {}
    # URI
    track_uri = track["track"]["uri"]

    # track name
    track_name = track["track"]["name"]
    song["name"] = (track_name)

    # artist info
    artist_uri = track["track"]["artists"][0]["uri"]
    artist_info = sp.artist(artist_uri)

    artist_name = track["track"]["artists"][0]["name"]
    artist_genres = artist_info["genres"]

    song["artist"] = (artist_name)
    song["genre"] = (artist_genres)

    # audio features
    features = sp.audio_features(track_uri)[0]
    song["bpm"] = int(features["tempo"])
    song["energy"] = (features["energy"])
    song["key"] = (features["key"])
    song["danceability"] = int((features["danceability"])*100)
    song["loudness"] = int(features["loudness"])

    song_data.append(song)