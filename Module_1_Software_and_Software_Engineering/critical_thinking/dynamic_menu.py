# Class to create and display dynamic menus for the task tracker application
class DynamicMenu:
    def __init__(self, menu_options, menu_type):
        self.menu_options = menu_options
        self.menu_type = menu_type

    # Function to display the menu template and get user input
    def display_template(self):
        print("\n" + "="*50 + "\n")
        print(f"\033[1;35m {self.menu_type} \033[0m".center(25))
        print()
        for key, value in self.menu_options.items():
            print(f"{key}. {value}")
        print("\n" + "="*50 + "\n")
        return input("Please select an option: ").upper()
