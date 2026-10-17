from datetime import datetime
from active_tasks_list import ActiveTasksList
from completed_tasks_list import CompletedTasksList


# Planning to create a task tracker

# This app will help users manage their tasks
# The users will be able to add, update, complete, and delete tasks

# Get users name



active_tasks_list = ActiveTasksList()
completed_tasks_list = CompletedTasksList()

# There will be a menu to view the active tasks and completed tasks 
    #Menu option will be View Active Tasks, View Completed Tasks, and Exit 
def main():
    user_name = input("Please enter your name: ")
    todays_date = datetime.now().strftime("%Y-%m-%d")
    
    print(f"\033[1;35m Hi {user_name}! Welcome back to the Todo App!\033[0m".center(50))
    print(f"\033[1;34m Today's date is {todays_date}\033[0m".center(50))
    
    while True:
        menu_option = display_menu()
        if menu_option =="A":
            handle_active_tasks()  # Call a function to handle active tasks actions
            
        elif menu_option == "C":
            handle_completed_tasks()  # Call a function to handle completed tasks actions
        elif menu_option == "Q":
            print("Have a great day!")
            break
        else:
            print("Invalid menu option. Please try again.")
        
    
def display_menu():
    
    menu = {"A": "View Active Tasks", "C": "View Completed Tasks", "Q": "Quit"}
    print("\n" + "="*50 + "\n")
    print(f"\033[1;35m MENU \033[0m".center(25))
    print()
    for key, value in menu.items():
        print(f"{key}. {value}")
    print("\n" + "="*50 + "\n")
    return input("Please select an option: ").upper()
    
def handle_active_tasks():
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
        completed_task = input("Enter the task you would like to mark as completed: ")
        if active_tasks_list.complete_task(completed_task):
            completed_tasks_list.add_completed_task(completed_task)
            print(f"Task '{completed_task}' marked as completed and moved to completed tasks.")
        else:
            print(f"Task '{completed_task}' not found.")
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


def handle_completed_tasks():
    print("Viewing Completed Tasks...")
    for completed_task in completed_tasks_list.get_completed_tasks():
        print(f"- {completed_task}")
        
    select_action = input("Enter D to delete a task or M to move a task back to active: ").upper()

    if select_action != "D" and select_action != "M":
        print("Invalid choice. Returning to menu.")
        display_menu()

    if select_action == "D":
        task_to_delete = input("Enter the task you would like to delete: ")
        completed_tasks_list.delete_task(task_to_delete)
        display_menu()

    if select_action == "M":
        task_to_move = input("Enter the task you would like to move back to active: ")
        completed_tasks_list.move_to_active(task_to_move, active_tasks_list)
        display_menu()
    
if __name__ == "__main__":
    main()