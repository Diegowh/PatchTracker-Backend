from .models import Episode, PatchNote, Content
from .scraper.services import scrap_data
from .scraper.version_fetcher import VersionFetcher


class DBManager:
    def __init__(self) -> None:
        self.episodes_data = VersionFetcher().episodes()