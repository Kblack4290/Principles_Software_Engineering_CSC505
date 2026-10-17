# Class to manage the list of active tasks in the task tracker application
class ActiveTasksList:
    
    def __init__(self):
        self.active_tasks =list()
    
    # Function to add a new task to the active tasks list
    def add_task(self, task):
        self.active_tasks.append(task)
        print(f"Task '{task}' added to active tasks.")

    # Function to mark a task as completed and move it to the completed tasks list
    def complete_task(self, task, completed_tasks_list):
        if task in self.active_tasks:
            self.active_tasks.remove(task)
            completed_tasks_list.add_completed_task(task)
            print(f"Task '{task}' marked as completed and moved to completed tasks.")
        else:
            print(f"Task '{task}' not found in active tasks.")

    # Function to edit an existing task in the active tasks list
    def edit_task(self, task, new_task):
        if task in self.active_tasks:
            index = self.active_tasks.index(task)
            self.active_tasks[index] = new_task
            print(f"Task '{task}' has been updated to '{new_task}'.")
        else:
            print(f"Task '{task}' not found in active tasks.")

    # Function to retrieve the list of active tasks
    def get_active_tasks(self):
        return self.active_tasks
