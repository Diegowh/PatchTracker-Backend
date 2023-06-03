from .models import Episode, PatchNote, Content
from .scraper.services import all_episodes_data

class DBManager:
    def __init__(self) -> None:
        self.episodes_data = all_episodes_data()
        
    def create_episodes(self):
        for episode_data in self.episodes_data:
            episode_name = episode_data['episode_name']
            episode, created = Episode.objects.get_or_create(
                episode_name=episode_name,
            )
            
            if created:
                self.create_patch_notes(episode, episode_data['versions'])
                
                
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
                
                
    def create_content(self, patch_note, html_content):
        '''Creates content data for the database'''
        Content.objects.create(
            patch_note=patch_note,
            html_content=html_content,
        )
        
    def manage(self):
        self.create_episodes()