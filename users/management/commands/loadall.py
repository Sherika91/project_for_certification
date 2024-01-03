import os

from django.core.management import call_command
from django.core.management.base import BaseCommand

from config import settings


class Command(BaseCommand):
    help = "Loads fixtures from fixtures dir"
    fixtures_dir = settings.FIXTURES_DIR
    loaddata_command = "loaddata"
    filenames = [
        "alldata",
    ]

    def handle(self, *args, **options):
        for fixture_filename in self.filenames:
            call_command(
                self.loaddata_command, os.path.join(self.fixtures_dir, f"{fixture_filename}.json"))
