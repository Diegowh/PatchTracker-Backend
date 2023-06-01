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
        '''Check if the element is a comment.'''
        return isinstance(element, Comment)
    
    
    def soup_cleaner(self):
        '''Clean up the soup object and return the cleaned soup'''
        
        if self.soup is None:
            print('Soup object is None, unable to clean')
            return None
        
        div_main = self.soup.find('div', class_='mw-parser-output')
        tags_to_delete = ['svg', 'script', 'img']
        tags_to_replace = ['span', 'a']
        self._get_patch_elements(div_main)
        self._remove_tags(div_main, tags_to_delete)
        self._replace_tags(div_main, tags_to_replace)
        self._remove_comments(div_main)
        self._remove_review_div(div_main)
        
        print(div_main)
        
        return self.soup

    def _get_patch_elements(self, div_main):
        '''Remove elements until h2 tag is found'''
        for element in div_main:
            if isinstance(element, NavigableString):
                continue
            if element.name == 'h2':
                break
            else:
                element.decompose()
        
    def _remove_tags(self, div_main: NavigableString, tags: list):
        '''Remove specific tags.
        
        Args:
            div_main (BeautifulSoup object): The div main object to clean.
            tags (list): List of tags to remove
        '''
        for tag in tags:
            for element in div_main(tag):
                element.decompose()
                
    def _replace_tags(self, div_main: NavigableString, tags: list):
        '''Replace tags with their text content.'''
        
        for tag in tags:
            for element in div_main.find_all(tag):
                element.replace_with(element.get_text())
                
    def _remove_comments(self, div_main):
        '''Remove comments from div_main'''
        comments = div_main.find_all(text=self.is_comment)
        for comment in comments:
            comment.extract()
            
    def _remove_review_div(self, div_main):
        '''Removes div.reviews'''
        review_div = div_main.find('div', class_='reviews')
        try:
            review_div.decompose()
        except TypeError as e:
            print(f'div.reviews not found: {e}')
            pass

url = url_generator(PATCH_V)
scraper = Scraper(url)