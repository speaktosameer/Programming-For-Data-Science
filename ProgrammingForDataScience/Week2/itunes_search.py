import requests

def search_itunes(artist):
    url = "https://itunes.apple.com/search"

    params = {
        "term": artist,
        "media": "music",
        "limit": 5
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()

        return response.json()

    except requests.exceptions.ConnectionError:
        print("Error: No internet connection.")
        return None

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
        return None

    except requests.exceptions.RequestException:
        print("Error: Problem connecting to iTunes.")
        return None