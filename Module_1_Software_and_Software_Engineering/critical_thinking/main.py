from datetime import datetime
from active_tasks_list import ActiveTasksList
from completed_tasks_list import CompletedTasksList
from dynamic_menu import DynamicMenu


# Planning to create a task tracker
# The app will display a menu to manage active and completed tasks

# Initialize the active and completed tasks lists
active_tasks_list = ActiveTasksList()
completed_tasks_list = CompletedTasksList()

# Main function to run the task tracker application
# This function will display the main menu and handle user interactions

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
    
    dynamic_menu = DynamicMenu(
        menu_options={"A": "View Active Tasks", "C": "View Completed Tasks", "Q": "Quit"},
        menu_type="Main Menu"
    )
    return dynamic_menu.display_template()
    
def run_submenu(menu, actions, get_tasks, title):
    while True:
        print(f"\nViewing {title}...")
        for task in get_tasks():
            print(f"- {task}")

        choice = menu.display_template()
        if choice == "Q":
            break
        if choice not in actions:
            print("Invalid choice. Please try again.")
            continue

        prompts, method = actions[choice]
        method(*[input(prompt) for prompt in prompts])


def handle_active_tasks():
    # key -> (prompts whose answers are passed to the method, method to call)
    actions = {
        "A": (("Enter the task you would like to add: ",),
            active_tasks_list.add_task),
        "C": (("Enter the task you would like to mark as completed: ",),
            lambda task: active_tasks_list.complete_task(task, completed_tasks_list)),
        "E": (("Enter the task you would like to edit: ", "Enter the new task: "),
            active_tasks_list.edit_task),
    }
    menu = DynamicMenu(
        menu_options={"A": "Add a task", "C": "Complete a task",
                    "E": "Edit a task", "Q": "Quit to main menu"},
        menu_type="Active Tasks",
    )
    run_submenu(menu, actions, active_tasks_list.get_active_tasks, "Active Tasks")


def handle_completed_tasks():
    actions = {
        "D": (("Enter the task you would like to delete: ",),
            completed_tasks_list.delete_task),
        "M": (("Enter the task you would like to move back to active: ",),
            lambda task: completed_tasks_list.move_to_active(task, active_tasks_list)),
    }
    menu = DynamicMenu(
        menu_options={"D": "Delete a task", "M": "Move a task back to active",
                    "Q": "Quit to main menu"},
        menu_type="Completed Tasks",
    )
    run_submenu(menu, actions, completed_tasks_list.get_completed_tasks, "Completed Tasks")



if __name__ == "__main__":
    main()