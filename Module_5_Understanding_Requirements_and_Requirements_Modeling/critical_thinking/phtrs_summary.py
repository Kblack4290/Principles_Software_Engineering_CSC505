"""phtrs_summary.py - Summarize the PHTRS use case diagram.

Defines the actors, use cases, and relationships shown in the UML use case
diagram for the Pothole Tracking and Repair System (PHTRS), then prints each
actor with a short description of its use cases and a summary of the diagram
structure. See README.txt for the design assumptions.

Run with:  python phtrs_summary.py
"""
import textwrap

BOX_WIDTH = 78
BOLD_CYAN = "\033[1;96m"
RESET = "\033[0m"

# Actors: name -> type (Primary or Secondary) and a short description
actors = {
    "Citizen": {
        "type": "Primary",
        "description": "Resident who reports potholes and damage through the Citizen Portal.",
    },
    "Public Works Admin": {
        "type": "Primary",
        "description": "Authorized public works employee who manages reports and repairs "
                       "in the secure Admin Interface.",
    },
    "Repair Crew": {
        "type": "Primary",
        "description": "Field crew that logs repair work from the tablet or mobile interface.",
    },
    "Notification Service": {
        "type": "Secondary",
        "description": "External email service that sends confirmations and status messages.",
    },
}

# Use cases: name -> short description of what the use case does
use_cases = {
    "Log In": "Sign in to PHTRS. Every use case that needs a signed-in user includes it.",
    "Report Pothole": "Submit a street address, size (1 to 10), and location (e.g., middle of "
                      "road, curb). PHTRS assigns an ID, district, and repair priority.",
    "Upload Photo": "Optionally attach an image of the pothole to a report.",
    "View Report Status": "Track the status of previously submitted reports on the citizen "
                          "dashboard.",
    "Submit Damage Claim": "File a claim with contact information, type of damage (e.g., tire, "
                           "alignment, body), dollar amount, and evidence.",
    "View/Filter Potholes": "View reported potholes and filter them by district or repair "
                            "priority.",
    "Assign Repair Crew": "Assign a crew to a pothole and record the crew size and equipment "
                          "in its work order.",
    "Update Repair Status": "Set a pothole's status (work in progress, repaired, temporary "
                            "repair, not repaired). Crews also log hours and filler used.",
    "Generate Reports": "Produce summaries of potholes and repairs, such as counts by "
                        "district, priority, and status, and repair cost.",
}

# Associations drawn in the diagram: (actor, use case)
associations = [
    ("Citizen", "Report Pothole"),
    ("Citizen", "View Report Status"),
    ("Citizen", "Submit Damage Claim"),
    ("Public Works Admin", "View/Filter Potholes"),
    ("Public Works Admin", "Assign Repair Crew"),
    ("Public Works Admin", "Update Repair Status"),
    ("Public Works Admin", "Generate Reports"),
    ("Repair Crew", "Update Repair Status"),
    ("Notification Service", "Report Pothole"),
    ("Notification Service", "Submit Damage Claim"),
    ("Notification Service", "Assign Repair Crew"),
    ("Notification Service", "Update Repair Status"),
]

# <<include>> relationships: (base use case, included use case)
includes = [
    ("Report Pothole", "Log In"),
    ("View Report Status", "Log In"),
    ("Submit Damage Claim", "Log In"),
    ("View/Filter Potholes", "Log In"),
    ("Assign Repair Crew", "Log In"),
    ("Update Repair Status", "Log In"),
    ("Generate Reports", "Log In"),
]

# <<extend>> relationships: (extending use case, base use case)
extends = [
    ("Upload Photo", "Report Pothole"),
]

def use_cases_for(actor_name):
    """Return the names of the use cases associated with an actor, in diagram order."""
    return [use_case for name, use_case in associations if name == actor_name]

def check_model():
    """Raise ValueError if the diagram data uses an actor or use case that is not defined."""
    for actor_name, use_case in associations:
        if actor_name not in actors or use_case not in use_cases:
            raise ValueError(f"Unknown name in association: {actor_name} - {use_case}")
    for first, second in includes + extends:
        if first not in use_cases or second not in use_cases:
            raise ValueError(f"Unknown use case in relationship: {first} - {second}")
    for actor_name in actors:
        if not use_cases_for(actor_name):
            raise ValueError(f"Actor has no use cases: {actor_name}")

def print_border(title, text_lines, width=BOX_WIDTH):
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

    # Print each line of text, wrapped to fit; bullet lines get a hanging indent
    for line in text_lines:
        indent = "  " if line.startswith("- ") else ""
        wrapped_lines = textwrap.wrap(line, width=inner_width - 2, subsequent_indent=indent)
        if not wrapped_lines:
            wrapped_lines = [""]
        for part in wrapped_lines:
            print("| " + part.ljust(inner_width - 2) + " |")
    print(top)

def print_actors():
    """Print one box per actor with its description and associated use cases."""
    for actor_name, details in actors.items():
        linked = use_cases_for(actor_name)
        lines = [details["description"], f"Use cases ({len(linked)}):"]
        lines += [f"- {name}: {use_cases[name]}" for name in linked]
        print_border(f"{actor_name} ({details['type']} Actor)", lines)
        print()

def build_summary_lines():
    """Return the lines for the diagram structure summary."""
    primary = [name for name, details in actors.items() if details["type"] == "Primary"]
    secondary = [name for name, details in actors.items() if details["type"] == "Secondary"]
    lines = [
        f"Actors: {len(actors)} ({len(primary)} primary, {len(secondary)} secondary)",
        f"Use cases: {len(use_cases)}",
        f"Actor-to-use-case associations: {len(associations)}",
        f"<<include>> relationships: {len(includes)}",
        f"<<extend>> relationships: {len(extends)}",
    ]

    # Group the include relationships by the use case that is included
    for target in dict.fromkeys(second for _first, second in includes):
        bases = [first for first, second in includes if second == target]
        lines.append(f"{target} is included by: {', '.join(bases)}")
    for extension, base in extends:
        lines.append(f"{extension} extends {base}")

    # Report use cases that more than one primary actor can start
    for name in use_cases:
        owners = [a for a, u in associations if u == name and actors[a]["type"] == "Primary"]
        if len(owners) > 1:
            lines.append(f"{name} is shared by: {', '.join(owners)}")
    return lines

def main():
    """Validate the diagram data, then print each actor and the structure summary."""
    check_model()
    print()
    print_actors()
    print_border("Diagram Structure Summary", build_summary_lines())

if __name__ == "__main__":
    main()
