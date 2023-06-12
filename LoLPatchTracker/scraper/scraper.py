from utils import soup, BASE_URL

class LoLScraper:
    def __init__(self) -> None:
        self.soup = soup(BASE_URL)
        self.seasons = self._seasons()
            
    def _seasons(self):
        seasons = [season for season in self._get_season_endpoints()]
        return seasons
        
    def _find_seasons_ul(self):
        '''Finds Seasons ul tag from soup'''
        span = self.soup.find('span', class_= 'mw-headline')
        h2 = span.find_parent('h2')
        ul = h2.find_next_sibling('ul')
        return ul.find_all('li')
    
    def _get_season_endpoints(self):
        '''Returns a dictionary with all seasons names and their endpoint.'''
        endpoint_dict = {}
        for li in self._find_seasons_ul():
            a_tag = li.find('a')
            if a_tag:
                endpoint_dict[a_tag.text] = a_tag.get('href')
            else:
                print("No A tag found.")
        return endpoint_dict