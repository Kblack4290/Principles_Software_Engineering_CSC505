"""Reusable menu display for the Terminal Task Tracker."""

# Dynamic menu class for the task tracker application

# Constants for menu display formatting
MENU_WIDTH = 50
TITLE_COLOR = "\033[1;35m"
RESET_COLOR = "\033[0m"

# Class for creating and displaying dynamic menus
class DynamicMenu:
    """Build and display a menu from a dictionary of options.

    Attributes:
        menu_options (dict[str, str]): Maps each menu key to its label.
        menu_type (str): Title shown above the options.
    """
    def __init__(self, menu_options, menu_type):
        """Store the options and the title for this menu."""
        self.menu_options = menu_options
        self.menu_type = menu_type

    # Display the menu template and return the user's choice
    def display_template(self):
        """Print the menu and return the user's choice in upper case.

        Returns:
            str: The key the user typed, converted to upper case.
        """
        
        border = "=" * MENU_WIDTH
        print(f"\n{border}\n")
        print(f"{TITLE_COLOR} {self.menu_type} {RESET_COLOR}".center(25))
        print()
        for key, label in self.menu_options.items():
            print(f"{key}. {label}")
        print(f"\n{border}\n")
        return input("Please select an option: ").upper()
