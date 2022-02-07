# statements
team = list()
player = dict()
matchgoals = list()
sumgoals = cod = 0

#input
while True:
    player['name'] = input("Enter the player's name: ").strip().capitalize()
    count = int(input(f"How many football match {player['name']} has played? "))
    for c in range(1, count+1):
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
print("-="*30)
print(f"{'cod':<4} {'nome':<15} {'goals':<30} {'total'}")
print("-"*60)
print(team)
for data in team:
    print(f"{cod:<4} {data['name']:<15} {data['goals']:<30} {sumgoals}")
    cod += 1

