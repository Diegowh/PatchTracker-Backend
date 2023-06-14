from PatchTrackerApp.utils import url_generator, soup
from django.conf import settings
from bs4 import Tag


    
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
        for i, url in enumerate(self._patches_urls()):
            tbody_soup = soup(url)
            tbodies = tbody_soup.find_all('tbody')
            
            if len(tbodies) != 2:
                raise ValueError('HTML contains more than 2 tbody elements.')
            
            # Obtener el nombre de la season para el dict de tbody
            season_name = url.split('#')[-1] if '#' in url else url.split('/')[-1]
            if i % 2 == 0: # Indices pares
                all_tbody[season_name] = tbodies[0]
            else:
                all_tbody[season_name] = tbodies[1]
        
        return all_tbody
    
    def _season_patches_data(self):
        all_seasons_patches = {}
        for season, tbody in self._patches_tbody().items():
            
            rows = tbody.find_all('tr')[1:] # Omite el header
            
            season_patches_data = []
            
            for row in rows:
                date_and_url_element = row.find('th')
                date = date_and_url_element.get_text(strip=True)
                url = date_and_url_element.find('a', class_="external autonumber")['href']
                
                patch_element = row.find('td')
                patch = patch_element.get_text(strip=True)
                
                new_champion_element = patch_element.find_next('td')
                new_champion = new_champion_element.get_text(strip=True) if new_champion_element else None
                
                season_patches_data.append(
                    {
                        'date': date,
                        'patch': patch,
                        'new_champion': new_champion,
                        'url': url,
                    }
                )

            all_seasons_patches[season] = season_patches_data
        
        return all_seasons_patches

class NotesScraper:
    def __init__(self, url) -> None:
        self.url = url
    
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
        
        
class LoLScraper(PatchesScraper, NotesScraper):
    def __init__(self) -> None:
        pass
            

