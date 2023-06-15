from .scraper.scraper import LoLScraper
from .models import Season, Patch, Notes


class DBManager:
    def __init__(self) -> None:
        self.all_data = LoLScraper().all_seasons_data
        
    def _create_seasons(self):
        for season_name in self.all_data.keys():
            first_patch = self.all_data[season_name][-1]
            season, _ = Season.objects.update_or_create(
                name=season_name,
                defaults={'date': first_patch['date']}
            )
            self._create_patches(season, self.all_data[season_name])
    
    def _create_patches(self, season, patches):
        for patch_data in patches:
            patch, _ = Patch.objects.update_or_create(
                name=patch_data['patch'],
                season=season,
                defaults={
                    'date': patch_data['date'],
                    'new_champion': patch_data['new_champion'],
                    'url': patch_data['url']
                }
            )
            self._create_notes(patch, patch_data['notes'])
    
    def _create_notes(self, patch, html_notes):
        Notes.objects.update_or_create(
            patch=patch, 
            defaults={
                'html':html_notes,
            }
        )
    
    def update(self):
        self._create_seasons()