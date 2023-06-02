import pip._vendor.requests as requests
from utils import soup


URL = "https://valorant.fandom.com/wiki/Patch_Notes"

class VersionFetcher:
    def __init__(self) -> None:
        self.url = URL
        self.soup = soup(self.url)
        
    def