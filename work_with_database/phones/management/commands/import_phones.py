import csv
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csv_file:

            phone_reader = csv.reader(csv_file, delimiter=';')
            # skip caption
            next(phone_reader)

            for line in phone_reader:
                # Add info to model Phone
                row = Phone()
                row.name = line[1]
                row.image = line[2]
                row.price = line[3]
                row.release_date = line[4]
                row.lte_exists = line[5]
                row.save()
