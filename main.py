from functions import *

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

CLIENT_ID = config['CLIENT_ID']
CLIENT_SECRET = config['CLIENT_SECRET']
PLAYLIST_ID = config['PLAYLIST_ID']

ACCESS_TOKEN = get_access_token(CLIENT_ID, CLIENT_SECRET)
scrobble_playlist(PLAYLIST_ID, ACCESS_TOKEN)
