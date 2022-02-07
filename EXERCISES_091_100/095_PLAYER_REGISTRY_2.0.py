# statements
team = list()
player = dict()
match = list()
matchgoals = list()
sumgoals = 0

#input
while True:
    player['name'] = input("Enter the player's name: ").strip().capitalize()
    count = int(input(f"How many football match {player['name']} has played? "))
    for c in range(0, count):
        goals = int(input(f"    How many goals in the match {c}? "))
        sumgoals += goals
        matchgoals.append(goals)
    player['goals'] = matchgoals
    player['total'] = sumgoals
    while True:
        choice = input("Do you want to continue? [Y/N]").strip().upper()
        if choice not in ['Y', 'N']:
            print("ERROR! Please, answer only Y or N.")
        else:
            if choice == "Y":
                print("-=" * 60)
                break
            elif choice == "N":
                break
    team.append(player.copy())
    if choice == "N":
        break



