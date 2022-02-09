# library
from random import randint
from time import sleep

# statements
numbers = list()

# function
def drawing(lst):
    print(f"Drawing the list's {len(lst)} values: \033[1;34m", end = " ")
    for count in lst:
        sleep(0.5)
        print(count, end= " ")
    print()
def summing(lst):
    sum = 0
    for count in lst:
        if count%2==0:
            sum += count
    print(f"\033[1;38mThe numbers pairs' sum of the list {lst} is \033[1;34m{sum}.")


# input
values = int(input("\033[1;38mEnter the number of values to draw: "))

# processing
for count in range(0,values):
    number = randint(0,9)
    numbers.append(number)

#output
drawing(numbers)
summing(numbers)
