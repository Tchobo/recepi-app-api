"""
Django command to wait for the database de be available

"""

import time

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to greet."""
    def handle(self, *args, **options):
        self.stdout.write("Hello everybody. How are you?")
       
