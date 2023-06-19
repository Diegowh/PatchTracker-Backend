from PatchTrackerApp.utils import url_generator, soup
from django.conf import settings
from bs4 import Tag
import re

# Decorators
def check_tbodies(func):
    def wrapper(*args, **kwargs):
        tbodies = func(*args, **kwargs)
        if len(tbodies)!= 2:
            raise ValueError('HTML contains more than 2 tbody elements.')
        return tbodies
    return wrapper


# Scraper
class SeasonsScraper:
    def _seasons(self) -> dict[str, str]:
        '''Returns a dict of all season names and their endpoints since Season Nine'''
        all_season_endpoints =self._get_season_endpoints()
        valid_seasons = list(all_season_endpoints.keys())[:-11] # Para obtener desde la season 10.
        return {season: all_season_endpoints[season] for season in valid_seasons}
        
    def _find_seasons_ul(self) -> list[str]:
        '''Finds Seasons ul tag from soup'''
        seasons_soup = soup(settings.LOL_WIKI)
        span = seasons_soup.find('span', class_= 'mw-headline')
        h2 = span.find_parent('h2')
        ul = h2.find_next_sibling('ul')
        return ul.find_all('li')
    
    def _get_season_endpoints(self) -> dict[str, str]:
        '''Returns a dictionary with all seasons endpoint.'''
        endpoint_dict = {}
        for li in self._find_seasons_ul():
            a_tag = li.find('a')
            if a_tag:
                href = a_tag.get('href')
                endpoint_dict[a_tag.text] = href.split(')')[-1]
        return endpoint_dict


class PatchesScraper(SeasonsScraper):
    def _patches_urls(self) -> list[str]:
        '''Returns a list with all urls.'''
        urls = []
        endpoints = list(self._seasons().values())
        for endpoint in endpoints:
            urls.append(url_generator(settings.LOL_WIKI, endpoint))
            
            pre_season_endpoint = endpoint + '#Pre' + endpoint.replace('/', '-')
            urls.append(url_generator(settings.LOL_WIKI, pre_season_endpoint))
        
        return urls
    
    @check_tbodies
    def _patches_tbody(self) -> dict[str, str]:
        '''Returns a dict with seasons and preseasons tbody.'''
        all_tbody = {}
        for i, url in enumerate(self._patches_urls()):
            tbody_soup = soup(url)
            tbodies = tbody_soup.find_all('tbody')
            
            # Obtener el nombre de la season para el dict de tbody
            season_name = url.split('#')[-1] if '#' in url else url.split('/')[-1]
            if i % 2 == 0: # Indices pares
                all_tbody[season_name] = tbodies[0]
            else:
                all_tbody[season_name] = tbodies[1]
        
        return all_tbody
    
    def _season_patches_data(self) -> dict[str, list[str]]:
        all_seasons_patches = {}
        for season, tbody in self._patches_tbody().items():
            
            rows = tbody.find_all('tr')[1:] # Omite el header
            
            season_patches_data = []
            
            for row in rows:
                date_and_url_element = row.find('th')
                date = date_and_url_element.get_text(strip=True)
                
                date = re.sub(r'(\d{1,2})(\d{4})', r'\1 \2', date)
                date = date.split('[')[0].strip()
                
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
    def __init__(self, url: str) -> None:
        self.url = url
        self.parent_section = self._sections_container_cleaner()
        self.h1 = self._get_h1()
        self.notes_section = self._notes_section_cleaner()
        self.html = self._html_constructor()
    
    def _get_sections_container(self) -> Tag:
        '''Return the parent <section> tag with the patch note content.'''
        patchnote_soup = soup(self.url)
        return patchnote_soup.find('section')
    
    def _sections_container_cleaner(self) -> Tag:
        parent_section = self._get_sections_container()
        try:
            divs = [child for child in parent_section.children if isinstance(child, Tag) and child.name == 'div']
        except AttributeError:
            pass
        
        else:
            if len(divs) >= 2:
                divs[-1].decompose()
                divs[-2].decompose()
            
        return parent_section
    
    def _get_h1(self) -> Tag | None:
        try:
            h1_section = self.parent_section.section
            h1 = h1_section.h1
            return h1
        except AttributeError:
            return None

    
    def _notes_section_cleaner(self) -> Tag:
        section = self.parent_section.find_all('section')[1]
        try:
            section.aside.decompose()
        except AttributeError:
            pass
        
        try:
            section.button.decompose()
        except AttributeError:
            pass
        
        return section
    
    def _html_constructor(self) -> str:
        return str(self.h1) + str(self.notes_section)
        
        
        
class LoLScraper(PatchesScraper):
    def __init__(self) -> None:
        self.all_seasons_data = self._get_all_seasons_data()
    
    def _get_all_seasons_data(self) -> dict[str, list[str]]:
        all_seasons_data = self._season_patches_data()
        
        for _, patches in all_seasons_data.items():
            for patch in patches:
                url = patch['url']
                notes_scraper = NotesScraper(url)
                patch['notes'] = notes_scraper.html
                
        return all_seasons_data