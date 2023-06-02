from version_fetcher import VersionFetcher
from scraper import Scraper


def scrap_data():
    episodes = VersionFetcher().episodes()
    patch_endpoints = [version["patch_endpoint"] for episode in episodes for version in episode["versions"]]
    
    all_html = []
    for endopoint in patch_endpoints:
        scraper = Scraper(endopoint)
        patch_html = scraper.patch_html
        all_html.append(patch_html)
        
    return all_html

print(scrap_data())