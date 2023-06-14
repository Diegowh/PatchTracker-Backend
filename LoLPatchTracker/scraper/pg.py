import requests
from bs4 import BeautifulSoup

def url_generator(base_url:str, patch_endpoint: str):
    """Generates a URL for a specific url and endpoint."""
    return f"{base_url}{patch_endpoint}"


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

def patches_tbody() -> dict:
    '''Returns a dict with seasons and preseasons tbody.'''
    
    html_soup = soup("https://leagueoflegends.fandom.com/wiki/Patch_(League_of_Legends)/Season_Nine#Season_Nine")
    tbodys = html_soup.find_all('tbody')
    
    return len(tbodys)



def clean_html():
    url = "https://www.leagueoflegends.com/en-us/news/game-updates/patch-9-1-notes/"
    
    patchnote_soup = soup(url)
    sections_container = patchnote_soup.find('section')
    return sections_container

print(clean_html())