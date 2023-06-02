import pip._vendor.requests as requests
from utils import soup


URL = "https://valorant.fandom.com/wiki/Patch_Notes"

class VersionFetcher:
    def __init__(self) -> None:
        self.url = URL
        self.soup = soup(self.url)
        
    def episodes(self):
        center = self.soup.find('center')
        episodes = []
        p = center.find('p')
        p.extract()
        
        for table in center.find_all('table'):
            episode_data = {
                "episode_name": table.find('caption').text.replace('\n', ''),
                "versions": [],
            }
            for row in table.find_all('tr')[1:]: # ignore header row
                cols = row.find_all('td')
                if len(cols) == 3:
                    patch = cols[0].text.strip()
                    patch_endpoint = cols[0].find('a')['href'] if cols[0].find('a') else None
                    release_date = cols[1].text.strip()
                    
                    version = {
                        "patch": patch,
                        "patch_endpoint": patch_endpoint,
                        "release_date": release_date,
                    }
                    episode_data["versions"].append(version)
            episodes.append(episode_data)
        
        print(episodes)

version_fetcher = VersionFetcher()
version_fetcher.episodes()