# task_manager.py

class TaskManager:
    def __init__(self, db):
        self.db = db

    def add_task(self, priority, description):
        self.db.add_task(priority, description)

    def display_tasks(self):
        return self.db.get_tasks()

    def remove_task(self, task_id):
        self.db.delete_task(task_id)
