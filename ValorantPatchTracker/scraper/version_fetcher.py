import requests
from utils import soup


URL = "https://valorant.fandom.com/wiki/Patch_Notes"

class VersionFetcher:
    def __init__(self) -> None:
        self.url = URL
        self.soup = soup(self.url)
        
    def extract_center_tag(self):
        center = self.soup.find('center')
        p = center.find('p')
        p.extract()
        return center
        
    def extract_episode_data(self, table):
        episode_data = {
            "episode_name": table.find('caption').text.replace('\n', ''),
            "versions": [],
        }
        return episode_data
    
    def extract_version_data(self, row):
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
            return version
        
    def episodes(self):
        center = self.extract_center_tag()

        episodes = []
        for table in center.find_all('table'):
            episode_data = self.extract_episode_data(table)

            for row in table.find_all('tr')[1:]: # ignore header row
                version = self.extract_version_data(row)
                if version: 
                    episode_data["versions"].append(version)
                    
            episodes.append(episode_data)
            
        return episodes