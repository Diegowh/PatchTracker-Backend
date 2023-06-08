from django.core.management.base import BaseCommand
from ...db_manager import DBManager


class Command(BaseCommand):
    help = 'Updates database with the scraped data'
    
    
    def handle(self, *args, **options):
        db_manager = DBManager()
        db_manager.update()
        self.stdout.write(self.style.SUCCESS('Valorant Database sucessfully updated'))