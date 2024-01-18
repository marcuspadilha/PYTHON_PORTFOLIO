# function
def player(name, goals):
    return f"The player {name} scored {goals} goals. "


# input
firstname = input("Enter the player's name: ").strip().capitalize()
numbergoals = input("Enter the number of goals: ")

if numbergoals.isnumeric():
    numbergoals = int(numbergoals)
else:
    numbergoals = 0

if firstname == "":
    firstname = "Unknown"

print(player(firstname, numbergoals))
input()
