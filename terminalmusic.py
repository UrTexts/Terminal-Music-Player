  GNU nano 8.2                                     terminalmusic.py                                              
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API credentials
CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URI = "http://localhost:8888/callback"
SCOPE = "user-read-playback-state,user-modify-playback-state,user-library-read"

# Initialize Spotify Client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

def search_and_play(track_name):
    """Search for a track and play it."""
    results = sp.search(q=track_name, type='track', limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        track_uri = track['uri']
        print(f"Playing: {track['name']} by {track['artists'][0]['name']}")
        sp.start_playback(uris=[track_uri])
    else:
        print("No track found!")

# Example usage
if __name__ == "__main__":
    track = input("Enter a track name: ")
    search_and_play(track)




