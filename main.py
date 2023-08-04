from refresh_token import getRefreshToken
import requests
import re
import json
from get_song_remediations import *
import pandas as pd
from dotenv import load_dotenv
import os


token = getRefreshToken()
playlist_id = os.getenv("PLAYLIST_ID")

def get_song_id(songTitle, songArtist, searchType):
    try:
        songTitle = re.sub(r'\([^)]*\)|\[[^]]*\]', '', songTitle)
        url = "https://api.spotify.com/v1/search?q="+songTitle+"%20artist:"+songArtist+"&type="+searchType+"&limit=1"
        headers = {
            "Authorization" : "Bearer " + token,
        }
        response = requests.get(url, headers=headers)
        response_json = response.json()
        if response.status_code == requests.codes.ok:
            id = response_json["tracks"]['items'][0]['id']
            
        else:
            print('Request failed!')
        return id
    except IndexError:
        print("Error: List index out of range!")

        return False
    



def get_apple_ghana100():
    url = os.getenv("TOP10SCRAPPER")
    response = requests.get(url=url)
    response_json = response.json()
    return response_json


def add_song_to_playlist(playlist_id, track_uri,position=None):
    
    track_uri = f"spotify:track:{track_uri}"
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    if(position is None):
        data = {
            "uris": [track_uri],
            
        }
    else:
        data = {
            "uris": [track_uri],
            "position": position
        }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raise an error if status code is not 2xx
        print("Song added to the playlist successfully!")
    except requests.exceptions.HTTPError as error:
        print("Error adding song to the playlist:", error)
        print("Response text:", response.text)
    except json.JSONDecodeError as error:
        print("Error parsing response JSON:", error)
        print("Response text:", response.text)
   
def remove_all_songs_from_playlist(playlist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Get the current list of tracks in the playlist
    response = requests.get(url, headers=headers)
    response_json = response.json()
    tracks = response_json.get("items", [])

    # Extract the list of track URIs
    track_uris = [track["track"]["uri"] for track in tracks]

    # Remove all tracks from the playlist
    data = {
        "tracks": [{"uri": uri, "positions": [i]} for i, uri in enumerate(track_uris)]
    }
    response = requests.delete(url, headers=headers, json=data)

    if response.status_code == 200:
        print("All songs removed from the playlist successfully!")
    else:
        print("Error removing songs from the playlist:", response.text)

       

def main():
    remove_all_songs_from_playlist(playlist_id)
    top100 = get_apple_ghana100()
    positon=0
    
    for index,element in top100.items():
        id = get_song_id(element[0],element[1],"track")
        if(isinstance(id,str)):
            add_song_to_playlist(playlist_id,id,positon)
            positon+=1
        elif(isinstance(id,bool)):
            result = get_song_id_failsafe_case_split(element[0],element[1])
            if(result):
                positon+=1
            
def get_song_id_failsafe_case_split(song,artist):
    artist = split_case_string(artist)
    id = get_song_id(song,artist,"track")
    if(isinstance(id,str)):
           add_song_to_playlist(playlist_id,id)
           return True
    elif(isinstance(id,bool)):   
        return get_song_id_failsafe_comma_split(song,artist)
        
   
def get_song_id_failsafe_comma_split(song,artist):
    failed={}
    words = extract_words_from_string(artist)
    for index, word in enumerate(words):
        id = get_song_id(song,word,"track")
        if(isinstance(id,str)):
           add_song_to_playlist(playlist_id,id)
           return True
        elif(isinstance(id,bool) and index == len(words)-1):
            failed.update({index:{"Song":song,"Artist":word}}) 
            return False  
            
            

main()

