class ActiveTasksList:
    
    def __init__(self):
        self.active_tasks =list()
        
    def add_task(self, task):
        self.active_tasks.append(task)
        print(f"Task '{task}' added to active tasks.")

    def complete_task(self, task):
        if task in self.active_tasks:
            self.active_tasks.remove(task)
            print(f"Task '{task}' marked as completed.")
        else:
            print(f"Task '{task}' not found in active tasks.")
    
    def modify_task(self, task):
        if task in self.active_tasks:
            new_task = input(f"Enter the new description for task '{task}': ")
            index = self.active_tasks.index(task)
            self.active_tasks[index] = new_task
            print(f"Task '{task}' has been updated to '{new_task}'.")
        else:
            print(f"Task '{task}' not found in active tasks.")
        
    def get_active_tasks(self):
        return self.active_tasks
    
    
    