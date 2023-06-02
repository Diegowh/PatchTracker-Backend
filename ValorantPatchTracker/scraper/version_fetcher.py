import pip._vendor.requests as requests
from utils import soup


URL = "https://valorant.fandom.com/wiki/Patch_Notes"

class VersionFetcher:
    def __init__(self) -> None:
        self.url = URL
        self.soup = soup(self.url)
        
    def versions(self):
        versions = []
        center = self.soup.find('center')
        
        p = center.find('p')
        p.extract()
        
        for table in center.find_all('table'):
            version_data = {
                "episode_name": table.find('caption').text,
            }
            print(version_data)


version_fetcher = VersionFetcher()
version_fetcher.versions()