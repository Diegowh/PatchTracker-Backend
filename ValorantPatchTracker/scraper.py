import pip._vendor.requests as requests
from bs4 import BeautifulSoup, NavigableString, Comment
from utils import url_generator, PATCH_V

class Scraper():
    def __init__(self, url) -> None:
        self.url = url
        self.soup = self._soup()
        self.clean_soup = self.soup_cleaner()
        
    def _soup(self):
        """Fetches the webpage from the given URL and parses it using BeautifulSoup

        Returns:
            BeautifulSoup object: Parsed HTML of the webpage
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f'Request to {self.url} failed: e')
            return None
        
        soup = BeautifulSoup(response.text, 'html.parser')
    
        return soup


    def is_comment(self, element):
        return isinstance(element, Comment)
    
    
    def soup_cleaner(self):
        
        if self.soup is None:
            print('Soup object is None, unable to clean')
            return None
        
        div_main = self.soup.find('div', class_='mw-parser-output')

        for element in div_main:
            if isinstance(element, NavigableString):
                continue
            if element.name == 'h2':
                break
            else:
                element.decompose()
                
        
        for svg in div_main('svg'):
            svg.decompose()
            
        for script in div_main('script'):
            script.decompose()
            
        for img in div_main('img'):
            img.decompose()
            
        for a in div_main('a'):
            a.decompose()
            
        comments = div_main.find_all(text=self.is_comment)
        for comment in comments:
            comment.extract()
            
        print(div_main)
        # # Elimino tags <img> y <a>
        # for tag in div_main(True):
        #     if tag.name not in keep_tags:
        #         print(tag.name)
        #         tag.decompose()
        #     else:
        #         tag.attrs = {}

        return self.soup

url = url_generator(PATCH_V)
scraper = Scraper(url)