import requests
import os

CHARBORG_TWITCH_ID = "113269771"

def get_bttv_global_emotes():
    base_url = "https://api.betterttv.net/3/"
    endpoint = "cached/emotes/global"
    url = base_url + endpoint
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        
        data = response.json()
        return data
    
    except requests.exceptions.RequestException as e:
        print("Error connecting to the API:", e)
        return []

def get_bttv_channel_emotes(provider, provider_id):
    base_url = "https://api.betterttv.net/3/"
    endpoint = f"cached/users/{provider}/{provider_id}"
    url = base_url + endpoint
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        
        data = response.json()
        channel_emotes = data.get("channelEmotes", [])
        shared_emotes = data.get("sharedEmotes", [])
        return channel_emotes + shared_emotes
    
    except requests.exceptions.RequestException as e:
        print("Error connecting to the API:", e)
        return []
    
def get_twitch_global_emotes():
   base_url = "https://api.twitch.tv/helix"
   endpoint = "/chat/emotes/global"
   url = base_url + endpoint

   try:
       headers = {
           "Client-ID": "YOUR_TWITCH_CLIENT_ID",  # Replace with your Twitch Client ID
           "Authorization": "Bearer YOUR_TWITCH_ACCESS_TOKEN"  # Replace with your Twitch Access Token
       }
       response = requests.get(url, headers=headers)
       response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        
       data = response.json()
       return data
    
   except requests.exceptions.RequestException as e:
       print("Error connecting to the Twitch API:", e)
       return []

def get_twitch_channel_emotes(provider_id):
   base_url = "https://api.twitch.tv/helix"
   endpoint = f"/chat/emotes/?broadcaster_id={provider_id}"
   url = base_url + endpoint

   try:
       response = requests.get(url)
       response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        
       data = response.json()
       return data
    
   except requests.exceptions.RequestException as e:
       print("Error connecting to the Twitch API:", e)
       return []

# TODO: Call all emotes and save to CSV file, headers [text, url, vendor]
# TODO: Use polars?