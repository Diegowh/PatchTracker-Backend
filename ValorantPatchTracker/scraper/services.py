from version_fetcher import VersionFetcher
from scraper import Scraper


def scrap_data():
    episodes = VersionFetcher().episodes()
    patch_endpoints = [version["patch_endpoint"] for episode in episodes for version in episode["versions"]]
    
    for endopoint in patch_endpoints:
        scraper = Scraper(endopoint)