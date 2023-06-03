from .version_fetcher import VersionFetcher
from .scraper import Scraper


def scrap_data():
    '''Returns a list'''
    episodes = VersionFetcher().episodes()
    
    for episode in episodes:
        for version in episode['versions']:
            scraper = Scraper(version['patch_endpoint'])
            version['content'] = scraper.patch_html
        
    return episodes