# statements
team = list()
player = dict()
matchgoals = list()
sumgoals = 0

# input
while True:
    player.clear()
    player['name'] = input("Enter the player's name: ").strip().capitalize()
    count = int(input(f"How many football match {player['name']} has played? "))
    for c in range(1, count + 1):
        goals = int(input(f"    How many goals in the match {c}? "))
        sumgoals += goals
        matchgoals.append(goals)
        goals = 0

    player['goals'] = matchgoals[:]
    matchgoals.clear()
    player['total'] = sumgoals
    sumgoals = 0
    while True:
        choice = input("Do you want to continue? [Y/N]").strip().upper()
        if choice not in ['Y', 'N']:
            print("ERROR! Please, answer only Y or N.")
        else:
            if choice == "Y":
                print("-=" * 30)
                break
            elif choice == "N":
                break
    team.append(player.copy())
    if choice == "N":
        break
print("-=" * 30)
print("-"*50)
print("cod ", end=" ")
for i in player.keys():
    print(f"{i:<15}", end="")
print()
print("-"*50)
for k, v in enumerate(team):
    print(f"{k:<5}", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()

print()
print("-=" * 30)
while True:
    search = int (input("Show the data what player of? (-1 to stop)"))
    if search == -1:
        break
    if search> len(team):
        print(f"ERROR! there is not player with the code {search}!")
    else:
        print(f"---Survey of the player {team[search]['name']}")
        for i, g in enumerate(team[search]['goals']):
            print(f"    In the match {i+1} the player made {g} goals.")
    print("-="*30)
print()