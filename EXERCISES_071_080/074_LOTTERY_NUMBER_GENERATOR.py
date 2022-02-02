#library
from random import randint
#processing
print("\033[1;38mThe numbers generated are : \033[1;33m")
numbers = (randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60))
#output
print(numbers)
print(f"\033[1;38mThe biggest value is {max(numbers)}.")
print(f"\033[1;38mThe smallest value is {min(numbers)}.")
input()