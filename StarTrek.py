import random 

# Constants 
MISSION_TYPES = ["Reconnaissance", "Trade Negotiation", "Hostile Encounter", "Evacuation", "Resource Mining"]

# Ship systems, resources, and crew 
ship = { 
    "systems": { 
        "shields": 100, 
        "weapons": 100, 
        "engines": 100, 
        "sensors": 100 
    }, 
    "resources": { 
        "energy": 1000, 
        "torpedoes": 10 
    }, 
    "crew": { 
        "Picard": "Command", 
        "Riker": "Command", 
        "Data": "Operations", 
        "Worf": "Operations", 
        "La Forge": "Operations", 
        "Crusher": "Sciences", 
        "Troi": "Sciences" 
    } 
}

def main(): 
    print("Welcome to the Star Trek: TNG Mission Simulator!") 
    score = 0 
    turns = 0 

    while True: 
        display_status() 
        action = get_user_action() 

        if action == "1": 
            score += run_mission() 
        elif action == "2": 
            repair_system() 
        elif action == "3": 
            add_crew_member() 
        elif action == "4": 
            print(f"Simulation ended. Final score: {score}") 
            break 
        else: 
            print("Invalid action. Please try again.\n")

        turns += 1 
        handle_random_event() 

        if turns % 3 == 0: 
            replenish_resources() 

def display_status(): 
    print("Current ship status:\n")
    for system, name in ship.items():
        print(f"{system.capitalize()}:")
        for resource, value in name.items():
            print(f"    {resource.lower()} = {value}")
    print("")

def get_user_action(): 
    print("\nWhat would you like to do?\n")
    print("1: Start a mission")
    print("2: Repair a system")
    print("3: Add crew member")
    print("4: End simulation")

    action = input("Enter your choice: ").strip()
    if action in ["1", "2", "3", "4"]:
        return action
    else:
        print("Error: invalid selection. Please try again.\n")
        return get_user_action()

def run_mission(): 
    mission_type = random.choice(MISSION_TYPES) 
    print(f"New mission: {mission_type}\n")

    if mission_type=="Explore":
        # TODO: Implement mission logic for different mission types
        print("You discovered a new planet. +50 points\n")
        # return the score earned from the mission
        return 50
    elif mission_type=="Negotiation":
        print("Successful negotiation with an alien species. +100 points\n")
        return 100
    elif mission_type=="Combat":
        print("Engaged in combat. +200 points\n")
        return 200
    elif mission_type=="Rescue":
        print("Rescue mission complete. +75 points\n")
        return 75
    else: 
        print("Mining for resources completed. +40 points\n")
        return 40

def repair_system(): 
    print("\nWhich system would you like to repair?\n")
    for system, status in ship["systems"].items():
        print(f"- {system.capitalize()}: {status}%")

    system_choice = input("\nEnter the system to repair: ").lower()
    if system_choice in ship["systems"]:
        if ship["systems"][system_choice] < 100:
            ship["systems"][system_choice] = 100
            print(f"{system_choice.lower()} has been repaired to 100%.\n")
        else:
            print(f"{system_choice.lower()} is already at full capacity.\n")
    else:
        print("Invalid choice. Please try again.\n")

def add_crew_member(): 
    print("\nAdding a new crew member.\n")
    new_name = input("Enter new crew member's name: ").lower()
    new_role = input(f"Enter {new_name}'s role: ").lower()

    if new_name not in ship["crew"]:
        ship["crew"][new_name] = new_role
        print(f"Welcome to the crew, {new_name}.\n")
    else:
        print(f"{new_name} is already part of the crew.\n")

def handle_random_event():
    events = ["Weapons malfunction"]
    event = random.choice(events)
    
    if event == "Weapons malfunction":
        ship["systems"]["weapons"] -= 10
        print("\nRandom Event: Weapons malfunction! Weapons reduced by 10%.\n")

def use_resource(resource, amount): 
    available = ship["resources"].get(resource, 0)

    if available >= amount:
        ship["resources"][resource] -= amount
        remaining = ship["resources"][resource]
        print(f"{resource.capitalize()} decreased by {amount}. Remaining: {remaining}\n")
    else:
        print(f"Insufficient {resource}. {amount} required. (You will need {amount - available} more to perform this task.)\n")

def replenish_resources(): 
    ship["resources"]["energy"] += 100
    ship["resources"]["torpedoes"] += 1

    if ship["resources"]["energy"] > 1000:
        ship["resources"]["energy"] = 1000
    if ship["resources"]["torpedoes"] > 10:
        ship["resources"]["torpedoes"] = 10

    print("Resources have been replenished:")
    print("+100 energy.\n+1 torpedoes.\n")

main()
