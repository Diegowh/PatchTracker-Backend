from utils import soup, BASE_URL

class LoLScraper:
    def __init__(self) -> None:
        self.soup = soup(BASE_URL)
        self.seasons = self._seasons()
            
    def _seasons(self):
        seasons = [li.text for li in self._find_seasons_ul() if li.text != '\n']
        return seasons
        
    def _find_seasons_ul(self):
        '''Finds Seasons ul tag from soup'''
        span = self.soup.find('span', class_= 'mw-headline')
        h2 = span.find_parent('h2')
        ul = h2.find_next_sibling('ul')
        return ul