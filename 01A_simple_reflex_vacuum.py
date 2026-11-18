# Practical 1A: Simple Reflex Agent - Vacuum Cleaner World

def simple_reflex_agent(location, status):
    """Choose an action using only the current location and current room status."""
    if status == "Dirty":
        return "Suck"
    if location == "A":
        return "Move Right"
    return "Move Left"


def run_vacuum_world():
    rooms = {"A": "Dirty", "B": "Dirty"}
    location = "A"

    print("Initial environment:", rooms)
    while "Dirty" in rooms.values():
        status = rooms[location]
        action = simple_reflex_agent(location, status)
        print(f"Location={location}, Status={status}, Action={action}")

        if action == "Suck":
            rooms[location] = "Clean"
        elif action == "Move Right":
            location = "B"
        elif action == "Move Left":
            location = "A"

    print("Final environment:", rooms)
    print("Both rooms are clean.")


if __name__ == "__main__":
    run_vacuum_world()
