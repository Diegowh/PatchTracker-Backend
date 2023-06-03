from .models import Episode, PatchNote, Content
from .scraper.services import all_episodes_data


class DBManager:
    def __init__(self) -> None:
        self.episodes_data = all_episodes_data()
        
    def _create_episodes(self):
        for episode_data in self.episodes_data:
            episode_name = episode_data['episode_name']
            episode, _ = Episode.objects.update_or_create(
                episode_name=episode_name,
            )
            
            self._create_patch_notes(episode, episode_data['versions'])
                
                
    def _create_patch_notes(self, episode, versions):
        for version_data in versions:
            version = version_data['patch']
            release_date = version_data['release_date']
            patch_note, _ = PatchNote.objects.update_or_create(
                version=version,
                episode=episode,
                defaults={'release_date': release_date}
            )
            
            self._create_content(patch_note, version_data['content'])
                
                
    def _create_content(self, patch_note, html_content):
        '''Creates content data for the database'''
        Content.objects.create(
            patch_note=patch_note,
            defaults={'html_content': html_content},
        )
        
    def update(self):
        self._create_episodes()