from version_fetcher import VersionFetcher


def scrap_data():
    episodes = VersionFetcher().episodes()
    patch_endpoints = [version["patch_endpoint"] for episode in episodes for version in episode["versions"]]
    
    