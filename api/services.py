import os
import time

import kaggle
import csv

from django.db import IntegrityError
from django.conf import settings
from django.db import transaction
from .models import *


# TODO
def download_csv_file_from_kaggle(name_of_dataset='heesoo37/120-years-of-olympic-history-athletes-and-results'):
    """Using auth with environment variable, read more: https://github.com/Kaggle/kaggle-api"""
    kaggle.api.authenticate()
    path = os.path.join(settings.BASE_DIR, '../api/csvfile')
    kaggle.api.dataset_download_files(name_of_dataset,
                                      path=path, unzip=True)


# TODO: change file_name
def insert_data(file_name="athlete_events", qtd=50):
    """
    :param qtd_rows: Quantity of rows to insert
    :return: list of objects to input
    """
    if Athlete.objects.count() > 0:
        last_row = Athlete.objects.latest('id').id
    else:
        last_row = 0
    max_id = last_row + qtd
    path = os.path.join(settings.BASE_DIR, '../api/csvfile/{}.csv'.format(file_name))
    with open(path, 'r') as f:
        reader = csv.DictReader(f, delimiter=',', quotechar='"')

        for row in reader:
            # NOTE(picolotoe): Avoid new tries to insert rows already exist
            if int(row["ID"]) <= last_row:
                continue
            # NOTE(picoloto): Replace values like NA to null
            for key, value in row.items():
                if key in ["Name", "Sex",  "Team", "NOC", "Games", "Season", "City", "Sport", "Event", "Medal"]:
                    if value == 'NA':
                        row[key] = "empty"
                else:
                    if value == 'NA':
                        row[key] = 0.0

            if int(row["ID"]) > max_id:
                break
            if Athlete.objects.filter(id=int(row['ID'])).exists():
                continue

            create_objects(row)


def create_objects(row):

    games = factory_to_check_exists(Games, row)
    team = factory_to_check_exists(Team, row)
    season = factory_to_check_exists(Season, row)
    city = factory_to_check_exists(City, row)
    sport = factory_to_check_exists(Sport, row)
    event = factory_to_check_exists(Event, row)
    medal = factory_to_check_exists(Medal, row)

    athlete = Athlete.objects.create(
        id=int(row["ID"]),
        name=row["Name"],
        sex=row["Sex"],
        games=games,
        team=team,
        season=season,
        city=city,
        sport=sport,
        event=event,
        medal=medal
    )
    with transaction.atomic():
        athlete.save()
    attribute = Attributes.objects.create(age=row["Age"], height=row["Height"],
                                          weight=row["Weight"], year=row["Year"], athlete=athlete)
    with transaction.atomic():
        attribute.save()


def factory_to_check_exists(object, row):
    print(object.__name__)
    attribute_name = object.__name__
    print(row[attribute_name])

    try:
        new_object = object.objects.create(name=row[attribute_name])
        with transaction.atomic():
            new_object.save()

    except IntegrityError:
        q_object = object.objects.filter(name=row[attribute_name])
        return q_object.first()
    return new_object

