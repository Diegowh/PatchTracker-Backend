from PatchTrackerApp.utils import url_generator, soup
from django.conf import settings


    
class SeasonsScraper:
    def _seasons(self) -> dict:
        '''Returns a dict of all season names and their endpoints since Season Nine'''
        all_season_endpoints =self._get_season_endpoints()
        valid_seasons = list(all_season_endpoints.keys())[:-10]
        return {season: all_season_endpoints[season] for season in valid_seasons}
        
    def _find_seasons_ul(self):
        '''Finds Seasons ul tag from soup'''
        seasons_soup = soup(settings.LOL_WIKI)
        span = seasons_soup.find('span', class_= 'mw-headline')
        h2 = span.find_parent('h2')
        ul = h2.find_next_sibling('ul')
        return ul.find_all('li')
    
    def _get_season_endpoints(self):
        '''Returns a dictionary with all seasons endpoint.'''
        endpoint_dict = {}
        for li in self._find_seasons_ul():
            a_tag = li.find('a')
            if a_tag:
                href = a_tag.get('href')
                endpoint_dict[a_tag.text] = href.split(')')[-1]
        return endpoint_dict


class PatchesScraper(SeasonsScraper):
    def _patches_urls(self) -> list:
        '''Returns a list with all urls.'''
        urls = []
        endpoints = list(self._seasons().values())
        for endpoint in endpoints:
            urls.append(url_generator(settings.LOL_WIKI, endpoint))
            
            pre_season_endpoint = endpoint + '#Pre' + endpoint.replace('/', '-')
            urls.append(url_generator(settings.LOL_WIKI, pre_season_endpoint))
        
        return urls
    
    def _patches_tbody(self) -> dict:
        '''Returns a dict with seasons and preseasons tbody.'''
        all_tbody = {}
        for url in self._patches_urls():
            tbody_soup = soup(url)
            tbody = tbody_soup.find('tbody')
            
            # Obtener el nombre de la season para el dict de tbody
            season_name = url.split('#')[-1] if '#' in url else url.split('/')[-1]
            
            all_tbody[season_name] = str(tbody)
        
        return all_tbody

class NotesScraper:
    def __init__(self, patch_endpoint) -> None:
        self.url = url_generator(settings.LOL_WIKI, patch_endpoint)
        
        
class LoLScraper(PatchesScraper, NotesScraper):
    def __init__(self) -> None:
        pass
            

