# library
from time import sleep
from random import randint
from operator import itemgetter

# statements
play = dict()
allgame = list()
ranking = dict()
# output, processing
for count in range(1, 5):
    sleep(0.5)
    result = randint(1, 6)
    print(f"\033[1;38mThe player {count} rolled \033[1;33m{result} \033[1;38min the dice. ")
    play[f'gamer {count}'] = result
allgame.append(play)
print("-=" * 30)

print(f"{'Ranking of the gamers ':=^30}")
ranking = sorted(play.items(), key=itemgetter(1), reverse=True)
for index, count in enumerate(ranking):
    sleep(0.5)
    print(f"  {index+1}º place: {count[0]} with {count[1]}")
input()