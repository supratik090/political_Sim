import requests
from constants import API_BASE_URL

def create_game(payload):
    response = requests.post(f"{API_BASE_URL}/api/games", json=payload, timeout=30)
    response.raise_for_status()
    return response.json()


def fetch_turn_view(game_id):
    response = requests.get(f"{API_BASE_URL}/api/games/{game_id}/turn-view", timeout=30)
    response.raise_for_status()
    return response.json()


def list_games(user_id=None):
    params = {}
    if user_id:
        params["userId"] = user_id
    response = requests.get(f"{API_BASE_URL}/api/games", params=params, timeout=30)
    response.raise_for_status()
    return response.json()


def advance_turn(game_id, payload):
    response = requests.post(f"{API_BASE_URL}/api/games/{game_id}/turn/advance", json=payload, timeout=30)
    response.raise_for_status()
    return response.json()


def forfeit_game(game_id):
    response = requests.post(f"{API_BASE_URL}/api/games/{game_id}/forfeit", timeout=30)
    response.raise_for_status()
    return response.json()


def api_get(path, params=None):
    response = requests.get(f"{API_BASE_URL}{path}", params=params, timeout=30)
    response.raise_for_status()
    return response.json()


def api_post(path, payload):
    response = requests.post(f"{API_BASE_URL}{path}", json=payload, timeout=30)
    response.raise_for_status()
    return response.json()


def api_put(path, payload):
    response = requests.put(f"{API_BASE_URL}{path}", json=payload, timeout=30)
    response.raise_for_status()
    return response.json()


def api_delete(path):
    response = requests.delete(f"{API_BASE_URL}{path}", timeout=30)
    response.raise_for_status()
    return response.json()


def fund_project(game_id, party_id, project_key, progress):
    response = requests.post(
        f"{API_BASE_URL}/api/games/{game_id}/parties/{party_id}/projects/fund",
        params={"projectKey": project_key, "progress": progress},
        timeout=30
    )
    response.raise_for_status()
    return response.json()


def set_project_target(game_id, party_id, project_key, target_party_id):
    response = requests.post(
        f"{API_BASE_URL}/api/games/{game_id}/parties/{party_id}/projects/{project_key}/target",
        params={"targetPartyId": target_party_id},
        timeout=30
    )
    response.raise_for_status()
    return response.json()
