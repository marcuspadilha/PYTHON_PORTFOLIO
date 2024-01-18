#library
from math import factorial

#input
number=int(input("Enter a number to calc its factorial: "))

#processin

print(f"Calculating {number}! = {number}",end="")
firstnumber = number
while number != 1:

    print(f" x {number-1}", end="")
    number = number - 1

print(f" = {factorial(firstnumber)}")
input()