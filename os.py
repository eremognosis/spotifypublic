import os
from spotipy.oauth2 import SpotifyOAuth

from dotenv import load_dotenv
load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")   ### i love secret clients
REDIRECT_URI = 'http://127.0.0.1:8000/'
SCOPE = 'user-read-recently-played' #  wer shall add more later (u can ADD whatever u want, u need nopt take my permision, u need not fikkiw me, be yourself, its individualism)

def get_my_refresh_token():
    sp_oauth = SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
        open_browser=False  #### ssh browsdes fdont hacee lol
    )


    refresh_token = sp_oauth.get_cached_token()['refresh_token']
    print(f"Touch grass :\n\n{refresh_token}\n") #### i mean redundant as for it saVWS a  .cache anyway

if __name__ == "__main__":
    get_my_refresh_token()