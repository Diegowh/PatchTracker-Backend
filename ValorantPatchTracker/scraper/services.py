from .version_fetcher import VersionFetcher
from .scraper import Scraper


def all_episodes_data():
    '''Returns a list with all episodes and patch data'''
    episodes = VersionFetcher().episodes()
    
    for episode in episodes:
        for version in episode['versions']:
            scraper = Scraper(version['patch_endpoint'])
            version['content'] = scraper.patch_html
        
    return episodes


print(all_episodes_data())