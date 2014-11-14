from __future__ import absolute_import

from celery.task import periodic_task
from datetime import timedelta

from cbrf_parser.management.commands._cbrf_parser import CbrfParser

@periodic_task(run_every = timedelta(seconds = 3600))
def parse_cbrf():
    print("CBRF parser is started")
    cbrf_parser = CbrfParser()
    cbrf_parser.load_data(1, False)


