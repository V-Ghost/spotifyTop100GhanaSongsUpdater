import requests
import re
import json
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime,timedelta,timezone
import base64
import time

def getRefreshToken():
    url = "https://accounts.spotify.com/api/token"
    client_id=""
    client_secret=""
    data = {
        "grant_type": "refresh_token",
        "refresh_token": "",
    }

    headers = {
        'Authorization': 'Basic ' + base64.b64encode(f'{client_id}:{client_secret}'.encode()).decode(),
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Convert the request body to JSON format
    # Send the POST request to refresh the access token
    response = requests.post(url, headers=headers, data=data)

    # Parse the JSON response and extract the new access token
    response_json = response.json()
    return response_json["access_token"]




def extract_words_from_string(string):
    words = string.split(',')
    words = [word.strip() for word in words]  # Remove leading/trailing whitespaces
    return words



def split_case_string(string):
    words = re.findall('[A-Z][a-z]*', string)
    result = ""
    for word in words:
        result = result + " " +word 
    return result


def get_song_id(songTitle, songArtist, searchType):
    token = getRefreshToken()
    try:
        songTitle = re.sub(r'\([^)]*\)|\[[^]]*\]', '', songTitle)
        url = "https://api.spotify.com/v1/search?q="+songTitle+"%20artist:"+songArtist+"&type="+searchType+"&limit=1"
        headers = {
            "Authorization": f"Bearer {token}",
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
    url = ""
    response = requests.get(url=url)
    response_json = response.json()
    return response_json


def add_song_to_playlist(playlist_id, track_uri,position=None):
    token = getRefreshToken()
    playlist_id = ""
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
    token = getRefreshToken()
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
def get_song_id_failsafe_comma_split(song,artist):
    failed={}
    words = extract_words_from_string(artist)
    print(words)
    for index, word in enumerate(words):
        print(word)
        id = get_song_id(song,word,"track")
        if(isinstance(id,str)):
           print("resolved in comma split")
           add_song_to_playlist("",id)
           print(id)
           return True
        elif(isinstance(id,bool) and index == len(words)-1):
            failed.update({index:{"Song":song,"Artist":word}})
            # df = pd.DataFrame(failed)
            # df.to_csv("failed_to_get_song_id_after_case_split.csv")  
            return False 
        
def get_song_id_failsafe_case_split(song,artist):
    artist = split_case_string(artist)
    id = get_song_id(song,artist,"track")
    if(isinstance(id,str)):
           print("resolved in case split")
           add_song_to_playlist("",id)
           print(id)
           return True
    elif(isinstance(id,bool)):   
        return get_song_id_failsafe_comma_split(song,artist)









default_args = {
    'start_date': datetime(2023, 5, 1),
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}


def clear():
    remove_all_songs_from_playlist("")
    time.sleep(3)
    

def get100songs(**context):
    top100 = get_apple_ghana100()
    context['ti'].xcom_push(key='top100', value=top100)

def getSongIdandAddtoPlaylist(**context):
    top100 = context['ti'].xcom_pull(key='top100')
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.post('http://52.23.174.181:5000/', data=json.dumps(top100), headers=headers)
    if response.status_code == 200:
        print('POST request successful')
    else:
        print('POST request failed')

with DAG('spotify', default_args=default_args, schedule_interval='0 3 * * *') as dag:
    clear_playlist_task = PythonOperator(
        task_id ='clear_task',
        python_callable=clear
    )

    get_songs_task = PythonOperator(
        task_id = 'get_songs_task',
        python_callable = get100songs
    )

    get_song_id_task_add_to_playlist = PythonOperator(
        task_id= 'get_song_id_task_add_to_playlist',
        python_callable = getSongIdandAddtoPlaylist
    )
    

    clear_playlist_task >> get_songs_task >> get_song_id_task_add_to_playlist

