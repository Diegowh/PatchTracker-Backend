from django.core.management import call_command
from django.core.management.base import BaseCommand
import time

class Command(BaseCommand):
    help = 'Updates both databases.'
    
    def handle(self, *args, **options):
        start_time_total = time.time()
        
        start_time_lol = time.time()
        call_command('update_lol')
        end_time_lol = time.time()
        lol_execution_time = round((end_time_lol - start_time_lol), 2)
        self.stdout.write(self.style.SUCCESS(f'in {lol_execution_time} seconds'))
        
        start_time_val = time.time()
        call_command('update_valorant')
        end_time_val = time.time()
        val_execution_time = round((end_time_val - start_time_val), 2)
        self.stdout.write(self.style.SUCCESS(f'in {val_execution_time} seconds'))
        
        
        end_time_total = time.time()
        total_execution_time = round((end_time_total - start_time_total), 2)
        self.stdout.write(self.style.SUCCESS(f'Both Databases successfully updated in {total_execution_time} seconds'))