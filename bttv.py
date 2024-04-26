import requests
import os

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
    
#def get_twitch_global_emotes():
#    base_url = "https://api.twitch.tv/helix"
#    endpoint = "/chat/emotes/global"
#    url = base_url + endpoint

#    try:
#        headers = {
#            "Client-ID": "YOUR_TWITCH_CLIENT_ID",  # Replace with your Twitch Client ID
#            "Authorization": "Bearer YOUR_TWITCH_ACCESS_TOKEN"  # Replace with your Twitch Access Token
#        }
#        response = requests.get(url, headers=headers)
#        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        
#        data = response.json()
#        return data
    
#    except requests.exceptions.RequestException as e:
#        print("Error connecting to the Twitch API:", e)
#        return []

#def get_twitch_channel_emotes(provider_id):
#    base_url = "https://api.twitch.tv/helix"
#    endpoint = f"/chat/emotes/?broadcaster_id={provider_id}"
#    url = base_url + endpoint

#    try:
#        response = requests.get(url)
#        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        
#        data = response.json()
#        return data
    
#    except requests.exceptions.RequestException as e:
#        print("Error connecting to the Twitch API:", e)
#        return []

# Example usage
bttv_global_emotes = get_bttv_global_emotes()
bttv_channel_emotes = []

#twitch_global_emotes = get_twitch_global_emotes()
#twitch_channel_emotes = []

provider = "twitch"  # Example provider
provider_id = "113269771"  # Example provider ID
bttv_channel_emotes = get_bttv_channel_emotes(provider, provider_id)
#twitch_channel_emotes = get_twitch_channel_emotes(provider_id)

# File paths
bttv_global_emotes_file = ""
bttv_channel_emotes_file = ""
#twitch_global_emotes_file = ""
#twitch_channel_emotes_file = ""

with open(bttv_global_emotes_file, "w") as file:
    for emote in bttv_global_emotes:
        file.write(emote['code'] + " " + emote['id'] + "\n")

with open(bttv_channel_emotes_file, "w") as file:
    for emote in bttv_channel_emotes:
        file.write(emote['code'] + " " + emote['id'] + "\n")

#with open(twitch_channel_emotes_file, "w") as file:
#    for emote in twitch_channel_emotes:
#        file.write(emote['code'] + " " + emote['id'] + "\n")

#with open(twitch_global_emotes_file, "w") as file:
#    for emote in twitch_global_emotes:
#        file.write(emote['code'] + " " + emote['id'] + "\n")

print("Emotes written to files: global_emotes.txt and channel_emotes.txt")
