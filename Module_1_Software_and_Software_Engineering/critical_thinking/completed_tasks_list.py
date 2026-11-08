"""Completed task storage and actions for the Terminal Task Tracker."""

# Class to manage the list of completed tasks in the task tracker application
class CompletedTasksList:
    """Manage the list of tasks that have been finished.

    Attributes:
        completed_tasks (list[str]): Tasks that have been marked as completed.
    """
    
    def __init__(self):
        """Start with an empty list of completed tasks."""
        self.completed_tasks = list()
    # Function to add a task to the completed tasks list
    def add_completed_task(self, task):
        """Add a finished task to the completed list."""
        self.completed_tasks.append(task)
        print(f"Task '{task}' added to completed tasks.")

    # Function to delete a task from the completed tasks list
    def delete_task(self, task):
        """Permanently remove a task from the completed list."""
        if task not in self.completed_tasks:
            print(f"Task '{task}' not found in completed tasks.")
            return
        
        self.completed_tasks.remove(task)
        print(f"Task '{task}' deleted from completed tasks.")

    # Function to move a completed task back to the active tasks list
    def move_to_active(self, task, active_tasks_list):
        """Send a completed task back to the active list.

        Args:
            task (str): The completed task to reopen.
            active_tasks_list (ActiveTasksList): Receives the reopened task.
        """
        if task not in self.completed_tasks:
            print(f"Task '{task}' not found in completed tasks.")
            return
        self.completed_tasks.remove(task)
        active_tasks_list.add_task(task)
        print(f"Task '{task}' moved back to active tasks.")
    
    def get_completed_tasks(self):
        """Return the list of completed tasks."""
        return self.completed_tasks