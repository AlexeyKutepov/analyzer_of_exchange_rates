__author__ = 'Alexey Kutepov'

from django.core.management.base import BaseCommand
from forecast.management.commands._optimization import  *

class Command(BaseCommand):

    def handle(self, *args, **options):
        best = hill_climb()
        for i in range(100):
            result = hill_climb(100, 30, "USD")
            if result[0] < best[0]:
                best = result
        print("best cost:",best[0],"best state: ",best[1])