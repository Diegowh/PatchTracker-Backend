from .scraper.scraper import LoLScraper
from .models import Season, Patch, Notes


class DBManager:
    def __init__(self) -> None:
        self.all_data = LoLScraper().all_seasons_data
        
    def _create_seasons(self):
        pass
    
    def _create_patches(self):
        pass
    
    def _create_notes(self):
        pass
    
    def update(self):
        pass