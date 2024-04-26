import requests
from typing import TypedDict, List

CHARBORG_TWITCH_ID = "113269771"


class Emote:
    id: str
    vendor: str
    text: str


class BTTVEmote(TypedDict):
    id: str
    code: str
    imageType: str
    animated: bool
    userId: str
    modifier: bool


# Gets the BTTV Global Emotes from their API
def get_bttv_global_emotes() -> List[Emote]:
    base_url = "https://api.betterttv.net/3/"
    endpoint = "cached/emotes/global"
    url = base_url + endpoint

    try:
        response = requests.get(url)
        response.raise_for_status()

        # Get the BTTV Emote list
        data: List[BTTVEmote] = response.json()
        # Massage into Emote
        emotes: List[Emote] = []
        for bttv_emote in data:
            emote_stripped: Emote = {
                "id": bttv_emote["id"],
                "vendor": "bttv",
                "text": bttv_emote["code"],
            }
            emotes.append(emote_stripped)
        return emotes

    except requests.exceptions.RequestException as e:
        print("Error connecting to the API:", e)
        return []


# Gets BTTV Channel emotes for a specific creator and provider
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


# Gets Twitch Global emotes based on API Authorization
def get_twitch_global_emotes(client_id, client_token):
    base_url = "https://api.twitch.tv/helix"
    endpoint = "/chat/emotes/global"
    url = base_url + endpoint

    try:
        headers = {"Client-ID": client_id, "Authorization": client_token}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        print("Error connecting to the Twitch API:", e)
        return []


# Gets Twitch Channel emotes based only on provider ID
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


# Gets all emotes and saves them to a CSV file
def get_all_emotes() -> List[Emote]:
    try:
        # First get the emotes
        bttv_global = get_bttv_global_emotes()
        # TODO: Fix authorization
        # twitch_channel = get_twitch_channel_emotes(CHARBORG_TWITCH_ID)
        return [*bttv_global]
    except Exception as e:
        print("Error getting all emotes", e)
        return []
