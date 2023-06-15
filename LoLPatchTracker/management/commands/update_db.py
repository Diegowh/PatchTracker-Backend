from django.core.management import call_command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Updates both databases.'
    
    def handle(self, *args, **options):
        call_command('update_lol')
        call_command('update_valorant')
        
        self.stdout.write(self.style.SUCCESS('Both Databases sucessfully updated'))