import sys
from datetime import datetime
from active_tasks_list import ActiveTasksList
#from completed_tasks_list import CompletedTasksList


# Planning to create a task tracker

# This app will help users manage their tasks
# The users will be able to add, update, complete, and delete tasks

# Get users name
user_name = input("Please enter your name: ")
todays_date = datetime.now().strftime("%Y-%m-%d")

active_tasks_list = ActiveTasksList()
#completed_tasks_list = CompletedTasksList()

# There will be a menu to view the active tasks and completed tasks 
    #Menu option will be View Active Tasks, View Completed Tasks, and Exit 
def main():
    print(f"\033[1;35m Hi {user_name}! Welcome back to the Todo App!\033[0m".center(50))
    print(f"\033[1;34mToday's date is {todays_date}\033[0m".center(50))
    display_menu()
    
def display_menu():
    
    menu = {"A": "View Active Tasks", "C": "View Completed Tasks", "Q": "Quit"}
    print("\n" + "="*50 + "\n")
    print(f"\033[1;35m MENU \033[0m".center(25))
    print()
    for key, value in menu.items():
        print(f"{key}. {value}")
    print("\n" + "="*50 + "\n")
    
    choice = input("Please select an option: ").upper()
    if choice == "A":
        print("Viewing Active Tasks...")
        for task in active_tasks_list.get_active_tasks():
            print(f"- {task}")
        
        select_action = input("Enter A to add a task, C to complete a task, or E to edit a task: ").upper()
        
        if select_action != "A" and select_action != "C" and select_action != "E":
            print("Invalid choice. Returning to menu.")
            display_menu()
            
        if select_action== "A":
            new_task = input("Enter the task you would like to add: ")
            active_tasks_list.add_task(new_task)
            for task in active_tasks_list.get_active_tasks():
                print(f"- {task}")
            display_menu()
        
        if select_action == "C":
            task_to_complete = input("Enter the task you would like to mark as completed: ")
            active_tasks_list.complete_task(task_to_complete)
            display_menu()
        
        if select_action == "E":
            task_to_edit = input("Enter the task you would like to edit: ")
            
            if task_to_edit not in active_tasks_list.get_active_tasks():
                print(f"Task '{task_to_edit}' not found in active tasks.")
                display_menu()
                return
            
            new_task = input("Enter the new task: ")
            active_tasks_list.edit_task(task_to_edit, new_task)
            for task in active_tasks_list.get_active_tasks():
                print(f"- {task}")
            display_menu()
            
        
    elif choice == "C":
        print("Viewing Completed Tasks...")
        
    elif choice == "Q":
        print("Exiting...")
        sys.exit()
    else:
        print("Invalid choice. Please try again.")
        display_menu()
    


# The Active todo class will display the list of active tasks
    # They will be able to add new tasks to the list and mark the tasks as completed

# The Completed todo class will display the list of completed tasks
    # They will be able to delete tasks from the list and move tasks back to the active list
    
    
    
if __name__ == "__main__":
    main()