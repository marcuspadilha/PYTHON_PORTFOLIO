#statements 
data = dict()
matchgoals = list()
sumgoals = 0
#input
data['name'] = input("Enter the player's name: ").strip().capitalize()
count = int(input(f"How many football match {data['name']} has played? "))
for c in range(0,count):
    goals = int(input(f"    How many goals in the match {c}? "))
    sumgoals += goals
    matchgoals.append(goals)
data['goals'] = matchgoals
data['total'] = sumgoals
print("=-"*30)
print(data)
print("=-"*30)
print(f"The player's name is {data['name']}.")
print(f"{data['name']} make per match {data['goals']} goals.")
print(f"In the total, the player did {sumgoals} goals")
print("=-"*30)
print(f"The player played {count} matches.")
for index,goals in enumerate(data['goals']):
    print(f"   => In the match {index}, {data['name']} did {goals} goals.")
print(f"{data['name']} did a total of {sumgoals} goals")

