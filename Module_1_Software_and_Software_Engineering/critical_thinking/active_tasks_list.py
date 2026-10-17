# The Active todo class will display the list of active tasks
    # They will be able to add new tasks to the list and mark the tasks as completed

class ActiveTasksList:
    
    def __init__(self):
        self.active_tasks =list()
        
    def add_task(self, task):
        self.active_tasks.append(task)
        print(f"Task '{task}' added to active tasks.")

    def complete_task(self, task):
        if task in self.active_tasks:
            self.active_tasks.remove(task)
            return True
        return False

    def edit_task(self, task, new_task):
        if task in self.active_tasks:
            index = self.active_tasks.index(task)
            self.active_tasks[index] = new_task
            print(f"Task '{task}' has been updated to '{new_task}'.")
        else:
            print(f"Task '{task}' not found in active tasks.")
        
    def get_active_tasks(self):
        return self.active_tasks
