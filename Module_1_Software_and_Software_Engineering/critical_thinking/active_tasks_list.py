"""Active task storage and actions for the Terminal Task Tracker."""

# Class to manage the list of active tasks in the task tracker application
class ActiveTasksList:
    """Manage the list of tasks that are still open.

    Attributes:
        active_tasks (list[str]): Tasks that have not been completed yet.
    """
    def __init__(self):
        """Start with an empty list of active tasks."""
        self.active_tasks =list()
    # Function to add a new task to the active tasks list
    def add_task(self, task):
        """Add a new task to the end of the active list."""
        self.active_tasks.append(task)
        print(f"Task '{task}' added to active tasks.")

    # Function to mark a task as completed and move it to the completed tasks list
    def complete_task(self, task, completed_tasks_list):
        """Move a task from the active list to the completed list.

        Args:
            task (str): The task to complete.
            completed_tasks_list (CompletedTasksList): Receives the finished task.
        """
        if task not in self.active_tasks:
            print(f"Task '{task}' not found in active tasks.")
            return

        self.active_tasks.remove(task)
        completed_tasks_list.add_completed_task(task)
        print(f"Task '{task}' marked as completed and moved to completed tasks.")

    # Function to edit an existing task in the active tasks list
    def edit_task(self, task, new_task):
        """Replace an existing task's text with new text, keeping its position.

        Args:
            task (str): The task to change.
            new_task (str): The replacement text.
        """
        if task not in self.active_tasks:
            print(f"Task '{task}' not found in active tasks.")
            return

        index = self.active_tasks.index(task)
        self.active_tasks[index] = new_task
        print(f"Task '{task}' has been updated to '{new_task}'.")

    # Function to retrieve the list of active tasks
    def get_active_tasks(self):
        """Return the list of active tasks."""
        return self.active_tasks
