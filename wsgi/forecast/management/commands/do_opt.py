__author__ = 'Alexey Kutepov'

from django.core.management.base import BaseCommand
from forecast.management.commands._optimization import  *

class Command(BaseCommand):

    def handle(self, *args, **options):
        best = hill_climb()
        for i in range(1000):
            result = hill_climb()
            if result[0] < best[0]:
                best = result
        print("best cost:",best[0],"best state: ",best[1])