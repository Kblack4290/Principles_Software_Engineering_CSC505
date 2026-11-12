"""
Black Adaptive Model builder.

Prompts the user for each phase name and a short description, then prints a
formatted summary of the model's phases, structure, and feedback loops.
"""
# Model configuration constants
MODEL_NAME = "Black Adaptive Model"
ITERATION_LENGTH = "2 weeks"
DEFAULT_PHASE_COUNT = 5  # Communication, Planning, Modeling, Construction, Deployment
DIVIDER_WIDTH = 60

# Define feedback loops for the model
FEEDBACK_LOOPS = [
    "Prototype review: customer reviews a prototype before construction (Modeling)",
    "Code defect: failing test from a coding bug loops back to Construction",
    "Design flaw: failing test from a wrong approach loops back to Modeling "
    "(or Planning if scope changes)",
    "Iteration feedback: customer demo feeds the next iteration's Communication phase",
]

# Helper functions for user input and phase collection
def get_non_empty_input(prompt):
    """Keep asking until the user enters something other than whitespace."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("This field can't be blank. Please try again.")

# Get the number of phases from the user
def get_phase_count():
    """Ask for the number of phases; Enter alone accepts the default."""
    while True:
        raw = input(
            f"How many phases does your model have? (press Enter for {DEFAULT_PHASE_COUNT}): "
        ).strip()
        if not raw:
            return DEFAULT_PHASE_COUNT
        try:
            count = int(raw)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if count >= 1:
            return count
        print("Please enter a number of 1 or more.")

# Collect phase names and descriptions from the user
def collect_phases(count):
    """Prompt for a name and description for each phase."""
    phases = []
    for i in range(1, count + 1):
        print(f"\n--- Phase {i} ---")
        name = get_non_empty_input(f"Enter the name of phase {i}: ")
        description = get_non_empty_input(f"Enter a short description of phase {i}: ")
        phases.append({"name": name, "description": description})
    return phases

# Print a summary of the model's phases, structure, and feedback loops
def print_summary(phases):
    """Print the phases, iteration structure, and feedback loops."""
    divider = "=" * DIVIDER_WIDTH

    print(f"\n{divider}")
    print(MODEL_NAME.upper().center(DIVIDER_WIDTH))
    print(divider)

    print("Phases (repeated every iteration):")
    for index, phase in enumerate(phases, start=1):
        print(f"Phase {index}: {phase['name']} - {phase['description']}")

    print("\nStructure:")
    print(f"  - Iteration length: {ITERATION_LENGTH}")
    print("  - Each iteration runs all phases in order, then ends with a customer demo")

    print("\nFeedback loops:")
    for number, loop in enumerate(FEEDBACK_LOOPS, start=1):
        print(f"  {number}. {loop}")

    print(divider)

# Main function to run the builder
def main():
    print(f"Welcome to the {MODEL_NAME} builder")
    count = get_phase_count()
    phases = collect_phases(count)
    print_summary(phases)


if __name__ == "__main__":
    main()
