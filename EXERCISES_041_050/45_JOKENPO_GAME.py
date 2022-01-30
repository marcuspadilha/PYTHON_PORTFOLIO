# library
from time import sleep
from random import randint
# input
print('''Your options:
[ 1 ] Stone
[ 2 ] Paper
[ 3 ] scissors''')
user = int(input("What is your choice? "))

# processing
print("\nJO\n")
sleep(0.5)
computer = randint(1,3)
print("KEN\n")
sleep(0.5)
print("PO!!!\n")

# output
if computer == 1:
    if user == 1 :
        print(f'''You chose STONE and the computer chose STONE.\nThe play was a DRAW.''')
    elif user == 2 :
        print(f'''You chose PAPER and the computer chose STONE.\nYou win!''')
    elif user == 3 :
        print(f'''You chose SCISSORS and the computer chose STONE.\nThe computer wins!''')

elif computer == 2:
    if user == 1:
        print(f'''You chose STONE and the computer chose PAPER.\nThe computer wins!''')
    elif user == 2:
        print(f'''You chose PAPER and the computer chose PAPER.\nThe play was a DRAW.''')
    elif user == 3:
        print(f'''You chose SCISSORS and the computer chose PAPER.\nYou win!''')
else:
    if user == 1:
        print(f'''You chose STONE and the computer chose SCISSORS.\nYou win!''')
    elif user == 2:
        print(f'''You chose PAPER and the computer chose SCISSORS.\nThe computer wins!''')
    elif user == 3:
        print(f'''You chosen SCISSORS and the computer chose SCISSORS.\nThe play was a DRAW.''')

input()