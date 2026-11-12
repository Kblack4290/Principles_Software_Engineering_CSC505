"""Terminal Task Tracker: a command-line to-do list with active and completed tasks.

Run with:  python main.py
"""

from datetime import datetime
from active_tasks_list import ActiveTasksList
from completed_tasks_list import CompletedTasksList
from dynamic_menu import DynamicMenu

# Shared task lists used by every menu handler
active_tasks_list = ActiveTasksList()
completed_tasks_list = CompletedTasksList()

# Terminal color codes for headings and dates
HEADING_COLOR = "\033[1;35m"
DATE_COLOR = "\033[1;34m"
RESET_COLOR = "\033[0m"

# Display the main menu and return the user's choice
def display_menu():
    """Show the main menu and return the user's choice (upper case)."""
    dynamic_menu = DynamicMenu(
        menu_options={"A": "View Active Tasks", "C": "View Completed Tasks", "Q": "Quit"},
        menu_type="Main Menu",
    )
    return dynamic_menu.display_template()

# Run a submenu for a specific task list (active or completed)
def run_submenu(menu, actions, get_tasks, title):
    """Run a task submenu until the user chooses Q.

    Args:
        menu (DynamicMenu): The submenu to display each loop.
        actions (dict): Maps a menu key to (prompts, method). The answers to the
            prompts are passed to the method as positional arguments.
        get_tasks (callable): Returns the tasks to list above the menu.
        title (str): Name of the list being shown, used in the heading.
    """
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

# Handle the Active Tasks submenu
def handle_active_tasks():
    """Run the Active Tasks submenu (add, complete, and edit tasks)."""
    # Create the actions and menu for the Active Tasks submenu
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

# Handle the Completed Tasks submenu
def handle_completed_tasks():
    """Run the Completed Tasks submenu (delete or reopen tasks)."""
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


# Main menu key -> function that handles it ("Q" is handled separately in main)
MAIN_MENU_HANDLERS = {
    "A": handle_active_tasks,
    "C": handle_completed_tasks,
}

# Display the welcome message with the user's name and today's date
def show_welcome(user_name):
    """Print the welcome banner with the user's name and today's date."""
    todays_date = datetime.now().strftime("%Y-%m-%d")
    print(f"{HEADING_COLOR} Hi {user_name}! Welcome back to the Todo App!{RESET_COLOR}".center(50))
    print(f"{DATE_COLOR} Today's date is {todays_date}{RESET_COLOR}".center(50))

# Main function to run the task tracker application
def main():
    """Greet the user, then show the main menu until they choose to quit."""
    user_name = input("Please enter your name: ")
    show_welcome(user_name)

    while True:
        menu_option = display_menu()
        if menu_option == "Q":
            print("Have a great day!")
            break
        handler = MAIN_MENU_HANDLERS.get(menu_option)
        if handler is None:
            print("Invalid menu option. Please try again.")
            continue
        handler()


if __name__ == "__main__":
    main()
