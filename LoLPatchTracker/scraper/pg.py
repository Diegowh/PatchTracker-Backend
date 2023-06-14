import requests
from bs4 import BeautifulSoup, Tag

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



url = "https://www.leagueoflegends.com/en-us/news/game-updates/patch-9-1-notes/"
    
class NotesScraper:
    def __init__(self, url) -> None:
        self.url = url
        self.parent_section = self._sections_container_cleaner()
        self.h1 = self._get_h1()
        self.notes_section = self._notes_section_cleaner()
        self.html = self._html_constructor()
        
    
    def _get_sections_container(self):
        '''Return the parent <section> tag with the patch note content.'''
        patchnote_soup = soup(self.url)
        return patchnote_soup.find('section')
    
    def _sections_container_cleaner(self):
        parent_section = self._get_sections_container()
        divs = [child for child in parent_section.children if isinstance(child, Tag) and child.name == 'div']
        
        if len(divs) >= 2:
            divs[-1].decompose()
            divs[-2].decompose()
            
        return parent_section
    
    def _get_h1(self):
        h1_section = self.parent_section.section
        return h1_section.h1
    
    def _notes_section_cleaner(self):
        section = self.parent_section.find_all('section')[1]
        section.aside.decompose()
        section.button.decompose()
        
        return section
    
    def _html_constructor(self):
        return str(self.h1) + str(self.notes_section)
        
        
        
note_scraper = NotesScraper(url=url)
print(note_scraper.html)