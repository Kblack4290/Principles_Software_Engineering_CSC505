"""shopping_list_prototype.py - Describe the Shopping List app prototype.

Defines the app's screens, the navigation flow between them, and example user
journeys, then prints a formatted summary of each. See the README for the
architecture diagram and the paper prototype (wireframe) screens.
"""
import textwrap

ARROW = "->"
BOLD_CYAN = "\033[1;96m"
RESET = "\033[0m"

# Screens: name -> short description of what the screen does
screens = {
    "Home": "Entry point. Shows the current list summary and buttons to add "
            "an item, view the list, see purchase history, or open settings.",
    "Add Item": "Form to enter an item name, quantity, optional price, "
                "category, and notes, then save it to the list.",
    "View List": "Shows all items with checkboxes, sort/filter options, "
                 "the running total, and the remaining budget.",
    "Edit / Delete Items": "Change an item's details or delete it from the list.",
    "View Purchase History": "Shows past shopping trips and frequent items, "
                             "with a Re-add button to put items back on the list.",
    "Settings / About": "Theme, units, currency, budget limit, reminders "
                        "toggle, and app information.",
}

# Navigation flow: (from screen, to screen, user action)
flow = [
    ("Home", "Add Item", "Tap + Add Item"),
    ("Home", "View List", "Tap View List"),
    ("Home", "View Purchase History", "Tap Purchase History"),
    ("Home", "Settings / About", "Tap Settings / About"),
    ("Add Item", "View List", "Save"),
    ("View List", "Edit / Delete Items", "Tap an item"),
    ("Edit / Delete Items", "View List", "Save / Delete"),
    ("View Purchase History", "View List", "Re-add items"),
]

# Example paths a user might take through the app.
example_journeys = [
    ["Home", "Add Item", "Save", "View List"],
    ["Home", "View List", "Edit / Delete Items", "Save / Delete", "View List"],
    ["Home", "View Purchase History", "Re-add items", "View List"],
]

def check_flow(screen_names, flow_steps):
    """Raise ValueError if any navigation step uses a screen that is not defined."""
    for start, end, _action in flow_steps:
        if start not in screen_names or end not in screen_names:
            raise ValueError(f"Unknown screen in flow: {start} {ARROW} {end}")

def print_border(title, text_lines, width=60):
    """Print a bordered section with a bold, colored title and word-wrapped lines.

    Args:
        title (str): Heading shown at the top of the box.
        text_lines (list[str]): Lines to print inside the box (wrapped to fit).
        width (int): Total width of the box in characters.
    """
    inner_width = width - 2
    top = "+" + "-" * inner_width + "+"
    centered_title = title.center(inner_width)
    print(top)
    print(f"|{BOLD_CYAN}{centered_title}{RESET}|")
    print(top)

    # Print each line of text, wrapped to fit within the inner width
    for line in text_lines:
        wrapped_lines = textwrap.wrap(line, width=inner_width - 2)
        if not wrapped_lines:
            wrapped_lines = [""]
        for part in wrapped_lines:
            print("| " + part.ljust(inner_width - 2) + " |")
        print("|" + " " * (inner_width) + "|")
    print(top)

def main():
    """Validate the navigation flow, then print screens, flow, journeys, and descriptions."""
    screen_names = list(screens.keys())
    check_flow(screen_names, flow)
    print()

    print_border(
        "Screens",
        [", ".join(screen_names), f"Total Screens: {len(screen_names)}"],
    )
    print()

    print_border(
        "Navigation Flow",
        [f"{start} {ARROW} {end}   ({action})" for start, end, action in flow],
    )
    print()

    print_border(
        "Example User Journeys",
        [f" {ARROW} ".join(journey) for journey in example_journeys],
    )
    print()

    print_border(
        "Screen Descriptions",
        [f"{name}: {description}" for name, description in screens.items()],
    )

if __name__ == "__main__":
    main()