# Dynamic menu class for the task tracker application

# Constants for menu display formatting
MENU_WIDTH = 50
TITLE_COLOR = "\033[1;35m"
RESET_COLOR = "\033[0m"

# Class for creating and displaying dynamic menus
class DynamicMenu:
    def __init__(self, menu_options, menu_type):
        self.menu_options = menu_options
        self.menu_type = menu_type

    # Display the menu template and return the user's choice
    def display_template(self):
        
        border = "=" * MENU_WIDTH
        print(f"\n{border}\n")
        print(f"{TITLE_COLOR} {self.menu_type} {RESET_COLOR}".center(25))
        print()
        for key, label in self.menu_options.items():
            print(f"{key}. {label}")
        print(f"\n{border}\n")
        return input("Please select an option: ").upper()
