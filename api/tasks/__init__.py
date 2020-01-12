from background_task.tasks import Task

from .tasks import task_update_data_from_kaggle, task_save_data_from_kaggle


task_update_data_from_kaggle(repeat=Task.DAILY)

task_save_data_from_kaggle(repeat=Task.DAILY)

print("start process started")