##########
### IMPORTS (coz ovb)
################
import os
from dotenv import load_dotenv
load_dotenv()
import pandas as pd
import os
import base64
import requests, logging
from time import time


def gerrt():
    """it givwes the accecc token"""
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    refresh_token = os.getenv("REFRESH_TOKEN")  # or shall i hardcode the passwoird? DM if you need my id
    
    if not all([client_id, client_secret, refresh_token]): # cute
        raise ValueError("Missing Environment Variables! Check GitHub Secrets.")

    # 2. Base64 Encode
    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()  ## beurocracy
    headers = {"Authorization": f"Basic {auth_header}"}
    
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }


    response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)  ### they woiulkd giuve iut
    
    if response.status_code != 200:
        logging.error(f"{time()}   Failed to refresh token: {response.text}") ### we wont check  but stol,
        exit(1)
        
    return response.json()['access_token']
