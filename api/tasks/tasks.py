from ..services import *

from background_task import background


@background(schedule=5)
def task_update_data_from_kaggle():
    print("Downloading data from kaggle...")
    download_csv_file_from_kaggle()


@background(schedule=15)
def task_save_data_from_kaggle():
    print("Inserting data in database...")
    save_data()
    print("Finished insert data.")
