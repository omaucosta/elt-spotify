#%%
import os
import spotipy
import json

from spotipy.oauth2 import SpotifyClientCredentials
from dotenv.main import load_dotenv



#%%
load_dotenv()
client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]
client_credentials = SpotifyClientCredentials(client_id, client_secret)

#%%
sp =  spotipy.Spotify(client_credentials_manager = client_credentials)
playlist = "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M?si=5d67f3d796864885"
url = playlist.split('/')[-1].split('?')[0]

#%%
results = sp.playlist_tracks(url)
results['items'][0]

#%%

playlist_json = json.dumps(results, indent=4)
print(playlist_json)

# %%
print(results['items'][0]['track']['album']['id'])
print(results['items'][0]['track']['album']['name'])
print(results['items'][0]['track']['album']['release_date'])
print(results['items'][0]['track']['album']['total_tracks'])
print(results['items'][0]['track']['album']['external_urls']['spotify'])

# %%

