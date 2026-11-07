# Class to manage the list of completed tasks in the task tracker application
class CompletedTasksList:
    
    def __init__(self):
        self.completed_tasks = list()
    # Function to add a task to the completed tasks list
    def add_completed_task(self, task):
        self.completed_tasks.append(task)
        print(f"Task '{task}' added to completed tasks.")

    # Function to delete a task from the completed tasks list
    def delete_task(self, task):
        if task not in self.completed_tasks:
            print(f"Task '{task}' not found in completed tasks.")
            return
        
        self.completed_tasks.remove(task)
        print(f"Task '{task}' deleted from completed tasks.")

    # Function to move a completed task back to the active tasks list
    def move_to_active(self, task, active_tasks_list):
        if task not in self.completed_tasks:
            print(f"Task '{task}' not found in completed tasks.")
            return
        self.completed_tasks.remove(task)
        active_tasks_list.add_task(task)
        print(f"Task '{task}' moved back to active tasks.")
    
    def get_completed_tasks(self):
        return self.completed_tasks