from rt import gerrt
import spotipy,os,json
from dotenv import load_dotenv
import pandas as pd
from time import time #### for nameing, for nothing is more uni ue anb progresisve as time, 4th dimension
import logging

OUTDATA = "spotifydata/rawjsons" ##### my windows ass literally wfucked up this earliwer after shifitng to linux frist
os.makedirs(OUTDATA, exist_ok=True)  #### sudo fiucket

load_dotenv()
token= gerrt()
sp = spotipy.Spotify(auth=token)
def getsavedata():
    res1 = sp.current_user_recently_played(limit=50) ### 50 is what their corporate asses allow, tho i can geyt prev by "next" (not entering that rabbit hole)

    with open(f"{OUTDATA}/{int(time())}.json","w") as f:
        json.dump(res1,fp=f, indent=4)
        logging.log(f"{time()} Done. Added {len(res1['items'])} songs. Good night") # we shall feed paranoifd

    
getsavedata()  ###  i could use __name__ but i didnt 
#### art thou blissfully ignorant of the socio economic powers of my progenitor?