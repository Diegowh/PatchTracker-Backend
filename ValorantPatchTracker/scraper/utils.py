import requests
from bs4 import BeautifulSoup


PATCH_ENDPOINT = "/wiki/Patch_Notes/1.02"
BASE_URL = "https://valorant.fandom.com/wiki/Patch_Notes/"

def patch_url_generator(patch_version: str):
    """Generates a URL for the patch notes of a specific version of Valorant"""
    return f"{BASE_URL}{patch_version}"


def soup(url):
    """Fetches the webpage from the given URL and parses it using BeautifulSoup

    Returns:
        BeautifulSoup object: Parsed HTML of the webpage
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f'Request to {url} failed: e')
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')

    return soup


