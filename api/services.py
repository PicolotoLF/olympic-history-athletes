import os

import kaggle
import csv

from django.conf import settings
from .models import *

# TODO
# 'heesoo37/120-years-of-olympic-history-athletes-and-results'
def download_csv_file_from_kaggle(name_of_dataset='heesoo37/120-years-of-olympic-history-athletes-and-results'):
    """Using auth with environment variable, read more: https://github.com/Kaggle/kaggle-api"""
    kaggle.api.authenticate()
    path = os.path.join(settings.BASE_DIR, '../api/csvfile')
    kaggle.api.dataset_download_files(name_of_dataset,
                                      path=path, unzip=True)


# TODO: change file_name
def insert_data(file_name="athlete_events", max_id=50):
    """
    :param qtd_rows: Quantity of rows to format
    :param from_line: The first line to format
    :return: list of objects to input
    """
    # Athlete.objects.all().delete()
    # Attributes.objects.all().delete()
    path = os.path.join(settings.BASE_DIR, '../api/csvfile/{}.csv'.format(file_name))
    with open(path, 'r') as f:
        reader = csv.DictReader(f, delimiter=',', quotechar='"')
        last_row = Athlete.objects.latest('id')
        for row in reader:
            # NOTE(picolotoe): Avoid new tries to insert rows already exist
            if int(row["ID"]) <= last_row.id:
                continue
            # TODO: Refactor, all this validations should be anothe function
            # NOTE(picolotoe): Replace values like NA to null
            for key, value in row.items():
                if value == 'NA':
                    row[key] = None
            if int(row["ID"]) > max_id:
                break

            if Athlete.objects.filter(id=int(row['ID'])).exists():
                continue

            athlete = Athlete.objects.create(
                id=int(row["ID"]),
                name=row["Name"],
                sex=row["Sex"],
            )
            attribute = Attributes.objects.create(age=row["Age"], height=row["Height"],
                                                  weight=row["Weight"], year=row["Year"], athlete=athlete)
            athlete.save()
            attribute.save()
