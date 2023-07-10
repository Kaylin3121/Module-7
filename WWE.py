# WWE Wrestlers Program

# Global Variables
wrestler_list = ["John Cena", "The Rock", "Triple H", "Undertaker"]  # List of WWE wrestlers
title_holder = "John Cena"  # Current WWE Champion
total_wrestlers = len(wrestler_list)  # Total number of wrestlers

# Function to display the list of wrestlers
def display_wrestlers():
    print("List of WWE Wrestlers:")
    for wrestler in wrestler_list:
        print(wrestler)

# Function to determine if a wrestler is the current champion
def is_champion(wrestler):
    if wrestler == title_holder:
        return True
    else:
        return False

# Decision Structure
def check_champion_status(wrestler):
    if is_champion(wrestler):
        print(wrestler, "is the current WWE Champion!")
    else:
        print(wrestler, "is not the current WWE Champion.")

# Repetition Structure
def count_wrestlers_with_initial(initial):
    count = 0
    for wrestler in wrestler_list:
        if wrestler.startswith(initial):
            count += 1
    return count

# Called Function
def get_total_wrestlers():
    return total_wrestlers

# Program Execution
print("Welcome to the WWE Wrestlers Program!")
print("Total number of wrestlers:", get_total_wrestlers())
display_wrestlers()
print("")

# Checking champion status
check_champion_status("The Rock")
check_champion_status("John Cena")
print("")

# Counting wrestlers with initial 'T'
initial = "T"
count = count_wrestlers_with_initial(initial)
print("Number of wrestlers with initial", initial + ":", count)

