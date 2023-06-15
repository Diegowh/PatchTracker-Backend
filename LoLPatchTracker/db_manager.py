from .scraper.scraper import LoLScraper
from .models import Season, Patch, Notes


class DBManager:
    def __init__(self) -> None:
        self.all_data = LoLScraper().all_seasons_data
        
    def _create_seasons(self):
        for season_name in self.all_data.keys():
            season, created = Season.objects.get_or_create(name=season_name)
            if created:
                first_patch = self.all_data[season_name][0]
                season.date = first_patch['date']
                season.save()
    
    def _create_patches(self):
        pass
    
    def _create_notes(self):
        pass
    
    def update(self):
        pass