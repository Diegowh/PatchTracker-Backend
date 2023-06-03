from .models import Episode, PatchNote, Content
from .scraper.services import all_episodes_data
from .scraper.version_fetcher import VersionFetcher


class DBManager:
    def __init__(self) -> None:
        self.episodes_data = all_episodes_data()
        
    def store_content(self, patch_note, html_content):
        '''Stores content data into the database'''
        Content.objects.create(
            patch_note=patch_note,
            html_content=html_content,
        )