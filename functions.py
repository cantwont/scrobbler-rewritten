import pylast
import time
import datetime
import json
import requests
import random

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

CLIENT_ID = config['CLIENT_ID']
CLIENT_SECRET = config['CLIENT_SECRET']
PLAYLIST_ID = config['PLAYLIST_ID']

LASTFM_API_KEY = config['LASTFM_API_KEY']
LASTFM_SHARED_SECRET = config['LASTFM_SHARED_SECRET']
LASTFM_USERNAME = config['LASTFM_USERNAME']
LASTFM_PASSWORD = config['LASTFM_PASSWORD']

NETWORK = pylast.LastFMNetwork(
    api_key=LASTFM_API_KEY,
    api_secret=LASTFM_SHARED_SECRET,
    username=LASTFM_USERNAME,
    password_hash=pylast.md5(LASTFM_PASSWORD),
)


def get_access_token(client_id, client_secret):
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    }

    response = requests.post('https://accounts.spotify.com/api/token', data=data)

    if response.status_code == 200:
        return response.json()['access_token']
    else:
        return ("Error: Client ID or Client Secret is incorrect\nHead to https://developer.spotify.com/dashboard to "
                "create an app")


def scrobble_playlist(playlist_id, token):
    headers = {
        'Authorization': f'Bearer {token}'
    }

    while True:
        response = requests.get(f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks', headers=headers)
        playlist_data = response.json()

        for item in playlist_data['items']:
            track_name = item['track']['name']
            artist_name = item['track']['artists'][0]['name']

            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")

            NETWORK.scrobble(artist=artist_name, title=track_name,
                             timestamp=int(time.mktime(datetime.datetime.now().timetuple())))

            print(f'Scrobbling {track_name} by {artist_name} at {current_time}')
            time.sleep(30 + random.randrange(1, 4))
