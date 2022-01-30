# library
from random import randint

# statement
count = 1

# input
print("I've just thought a number between 0 to 10.")
usernumber = int(input("Can you guess what number it was? "))

# processing
computernumber = randint(1,10)
while computernumber != usernumber:
    if computernumber > usernumber:
        usernumber=int(input("More... Try again: "))
        count += 1
    else:
        usernumber=int(input("Less... Try again: "))
        count += 1
print(f"\nyou got it right in {count} tries. Congratulations! ")