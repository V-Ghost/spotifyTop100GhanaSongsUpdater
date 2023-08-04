import requests
import json
import base64
from dotenv import load_dotenv
import os



def getRefreshToken():
    url = "https://accounts.spotify.com/api/token"
    client_id= os.getenve("CLIENT_ID")
    client_secret= os.getenv("CLIENT_SECRET")
    refresh_token = os.getenv("REFRESH_TOKEN")
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
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



