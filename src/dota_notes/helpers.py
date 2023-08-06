import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry


def get_game_live_stats(api_key, server_id):
    """Fetch game live information using the WEB API and knowing the server the game is played on.

    Args:
        api_key: str Steam WEB API key
        server_id: int Server ID where the match is played
    """
    try:
        s = requests.Session()
        retries = Retry(total=8, backoff_jitter=1, status_forcelist=[400])
        s.mount("https://", HTTPAdapter(max_retries=retries))
        url = f"https://api.steampowered.com/IDOTA2MatchStats_570/GetRealtimeStats/v1/?key={api_key}&server_steam_id={str(server_id)}"
        response = s.get(url)
        response.raise_for_status()

        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching data: {e}")
        return None
