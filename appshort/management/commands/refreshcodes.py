from django.core.management.base import BaseCommand, CommandError

from appshort.models import KirrUrl



class Command(BaseCommand):
    help = "Refresh all KirrUrl Short Codes"

    def add_arguments(self, parser):
        parser.add_argument('items', type = int)
    
    def handle(*args, **options):
        return KirrUrl.objects.refresh_shortcodes()

