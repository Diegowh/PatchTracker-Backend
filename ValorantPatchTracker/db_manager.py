from .models import Episode, PatchNote, Content
from .scraper.services import all_episodes_data
from .scraper.version_fetcher import VersionFetcher


class DBManager:
    def __init__(self) -> None:
        self.episodes_data = all_episodes_data()
        
    def create_content(self, patch_note, html_content):
        '''Creates content data for the database'''
        Content.objects.create(
            patch_note=patch_note,
            html_content=html_content,
        )
        
    def create_patch_notes(self, episode, versions):
        for version_data in versions:
            version = version_data['patch']
            release_date = version_data['release_date']
            patch_note, created = PatchNote.objects.get_or_create(
                version=version,
                release_date=release_date,
                episode=episode,
            )

            if created:
                self.create_content(patch_note, version_data['content'])