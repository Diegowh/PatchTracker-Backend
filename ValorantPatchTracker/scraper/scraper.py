from bs4 import NavigableString, Comment
from utils import patch_url_generator, PATCH_V, soup
from tag_remover import TagRemover

class Scraper(TagRemover):
    def __init__(self, url) -> None:
        self.url = url
        self.soup = soup(self.url)
        self.clean_soup = self._soup_cleaner()

    def is_comment(self, element):
        '''Check if the element is a comment.'''
        return isinstance(element, Comment)
    
    
    def _soup_cleaner(self):
        '''Clean up the soup object and return the cleaned soup'''
        
        if self.soup is None:
            print('Soup object is None, unable to clean')
            return None
        
        div_main = self.soup.find('div', class_='mw-parser-output')
        tags_to_remove = ['svg', 'script', 'img', ('div', 'reviews'), 'sup', ('div', 'mw-references-wrap'), 'ol']
        tags_to_remove_by_class = [('div', 'reviews'), ('div', 'mw-references-wrap')]
        tags_to_remove_by_text = [('h2', 'References'), ('p', 'The following')]
        tags_to_replace = ['span', 'a']
        
        self._get_patch_elements(div_main)
        
        for tag in tags_to_remove:
            self.remove_tag(div_main, tag)
        
        for tag, tag_class in tags_to_remove_by_class:
            self.remove_tag_by_class(div_main, tag, tag_class)
            
        for tag, text in tags_to_remove_by_text:
            self.remove_tag_by_text(div_main, tag, text)
        
        self._replace_tags(div_main, tags_to_replace)
        self._remove_comments(div_main)
        div_main = self._get_content(div_main)
        
        print(div_main)

        return div_main

    def _get_patch_elements(self, div_main):
        '''Remove elements until h2 tag is found'''
        for element in div_main:
            if isinstance(element, NavigableString):
                continue
            if element.name == 'h2':
                break
            else:
                element.decompose()
                
    def _replace_tags(self, div_main: NavigableString, tags: list):
        '''Replace tags with their text content.'''
        
        for tag in tags:
            for element in div_main.find_all(tag):
                element.replace_with(element.get_text())
                
    def _remove_comments(self, div_main):
        '''Remove comments from div_main'''
        comments = div_main.find_all(string=self.is_comment)
        for comment in comments:
            comment.extract()
            
    def _get_content(self, div_container):
        return ''.join(str(content) for content in div_container.contents)
    

patch_url = patch_url_generator('0.49')
scraper = Scraper(patch_url)