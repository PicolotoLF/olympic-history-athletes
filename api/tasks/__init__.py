from background_task.tasks import Task

from .tasks import update_data_from_kaggle, insert_data_from_kaggle


# update_data_from_kaggle(repeat=Task.DAILY)

insert_data_from_kaggle(repeat=Task.DAILY)

print("start process started")