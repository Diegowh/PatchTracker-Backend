from utils import soup, BASE_URL

class Scraper:
    def __init__(self) -> None:
        self.soup = soup(BASE_URL)
        
    def find_seasons_ul(self):
        '''Finds Seasons ul tag from soup'''
        span = self.soup.find('span', class_= 'mw-headline')
        h2 = span.find_parent('h2')
        ul = h2.find_next_sibling('ul')
        return ul