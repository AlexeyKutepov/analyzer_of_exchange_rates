__author__ = 'Alexey Kutepov'

from django.core.management.base import BaseCommand, CommandError
from forecast.management.commands._optimization import  *

class Command(BaseCommand):

    def handle(self, *args, **options):
        steps = 1
        if len(args) == 1:
            try:
                steps = int(args[0])
            except:
                raise CommandError("Incorrect arguments")

        best = hill_climb()
        for i in range(100):
            result = hill_climb(100, steps, "USD")
            if result[0] < best[0]:
                best = result
        print("best cost:",best[0],"best state: ",best[1])