from ..services import *

from background_task import background


@background(schedule=5)
def update_data_from_kaggle():
    print("Downloading data from kaggle...")
    download_csv_file_from_kaggle()


@background(schedule=120)
def insert_data_from_kaggle():
    print("Inserting data in database...")
    insert_data()
