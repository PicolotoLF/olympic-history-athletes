import os

import csv
import kaggle

from django.db import IntegrityError
from django.conf import settings
from .models import *


# TODO
def download_csv_file_from_kaggle(name_of_dataset='heesoo37/120-years-of-olympic-history-athletes-and-results',
                                  path='../api/csvfile'):
    """Using auth with environment variables, read more: https://github.com/Kaggle/kaggle-api"""
    kaggle.api.authenticate()
    join_path = os.path.join(settings.BASE_DIR, path)
    kaggle.api.dataset_download_files(name_of_dataset,
                                      path=join_path, unzip=True)


def format_data(file_name="athlete_events", qtd=50):
    """
    :param file_name: The name of the file to search in /api/csvfile
    :param qtd: Quantity of rows to insert
    :return: list
    """
    # NOTE(picoloto): Check if the table it's empty
    if Athlete.objects.count() > 0:
        last_row = Athlete.objects.latest('id').id
    else:
        last_row = 0
    max_id = last_row + qtd
    path = os.path.join(settings.BASE_DIR, '../api/csvfile/{}.csv'.format(file_name))
    results = []
    with open(path, 'r') as f:
        reader = csv.DictReader(f, delimiter=',', quotechar='"')
        last_id = 0
        for row in reader:
            # NOTE(picolotoe): Avoid new tries to insert rows already exist
            if int(row["ID"]) <= last_row or row["ID"] == last_id:
                continue
            # NOTE(picoloto): Clear the values
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
            last_id = row["ID"]
            results.append(row)
    return results


def save_data():
    list_of_objects = format_data()
    for object in list_of_objects:
        create_objects(object)


def create_objects(dict_from_csv):
    """
    :param dict_from_csv: row from csv file 
    :return: None
    """
    list_models = [Games, Team, Season, City, Sport, Event, Medal]
    results = {}
    for model in list_models:
        obj = factory_to_check_exists(model, dict_from_csv)
        results["{}".format(model.__name__)] = obj

    athlete = Athlete.objects.create(
        id=int(dict_from_csv["ID"]),
        name=dict_from_csv["Name"],
        sex=dict_from_csv["Sex"],
        games=results["Games"],
        team=results["Team"],
        season=results["Season"],
        city=results["City"],
        sport=results["Sport"],
        event=results["Event"],
        medal=results["Medal"]
    )

    attribute = Attributes.objects.create(age=dict_from_csv["Age"], height=dict_from_csv["Height"],
                                          weight=dict_from_csv["Weight"], year=dict_from_csv["Year"], athlete=athlete)

    athlete.save()
    attribute.save()


def factory_to_check_exists(object, row):
    """
    This factory check if the object that have the column "name" already exists,
    if not exists, return a new object
    :param object: object from model that have the column "name"
    :param row: row from csv to validate
    :return: if the object not exists on the table, return a new object,
    if exists, return the object
    """
    attribute_name = object.__name__

    try:
        result_object = object.objects.create(name=row[attribute_name])
        result_object.save()
    except IntegrityError:
        result_object = object.objects.filter(name=row[attribute_name]).first()
    return result_object
