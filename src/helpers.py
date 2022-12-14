"""
A collection of helper functions for devs.
"""
import time
import spotipy
from IPython.core.display import clear_output
from spotipy import SpotifyClientCredentials, util
import config
# Import revelant libraries

REDIRECT_URI = 'http://localhost:8888/callback'
SCOPE = 'playlist-modify-public'

# Credentials to access the Spotify Music Data
manager = SpotifyClientCredentials(config.CLIENT_ID, config.CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=manager)

# Credentials to access to the spotify user's playlist, favorite songs, etc.
token = util.prompt_for_user_token(
    config.USERNAME, SCOPE, config.CLIENT_ID, config.CLIENT_SECRET, REDIRECT_URI)
spt = spotipy.Spotify(auth=token)


def get_songs_features(ids):
    """
    Acquire the audio features of songs.

    Args:
        ids: A string representing the songs' ids.

    Returns:
        Each song track with its corresponding audio features.
    """

    meta = sp.track(ids)
    features = sp.audio_features(ids)

    # meta
    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity']
    ids = meta['id']

    # features
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    valence = features[0]['valence']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    key = features[0]['key']
    time_signature = features[0]['time_signature']

    track = [name, album, artist, ids, release_date, popularity, length,
             danceability, acousticness, energy, instrumentalness, liveness,
             valence, loudness, speechiness, tempo, key, time_signature]
    columns = ['name', 'album', 'artist', 'id', 'release_date', 'popularity',
               'length', 'danceability', 'acousticness', 'energy',
               'instrumentalness', 'liveness', 'valence', 'loudness',
               'speechiness', 'tempo', 'key', 'time_signature']
    return track, columns


def download_playlist(id_playlist, n_songs):
    """
    Acquire the audio features of songs in a given playlist with a limit of
    100 songs.

    Args:
        id_playlist: A string representing the playlist' id.
        n_songs: An integer representing the number of songs to download.

    Returns:
        Each song track with its corresponding audio features.
    """
    songs_id = []
    tracks = []

    for i in range(0, n_songs, 100):
        playlist = spt.playlist_tracks(id_playlist, limit=100, offset=i)

        for songs in playlist['items']:
            songs_id.append(songs['track']['id'])

    counter = 1
    for ids in songs_id:

        time.sleep(.6)
        track, columns = get_songs_features(ids)
        tracks.append(track)

        print(f"Song {counter} Added:")
        print(f"{track[0]} By {track[2]} from the album {track[1]}")
        clear_output(wait=True)
        counter += 1

    clear_output(wait=True)
    print("Music Downloaded!")

    return tracks, columns
