import sys
from datetime import datetime


# Planning to create a task tracker

# This app will help users manage their tasks
# The users will be able to add, update, complete, and delete tasks

#Get users name
user_name = input("Please enter your name: ")
todays_date = datetime.now().strftime("%Y-%m-%d")

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