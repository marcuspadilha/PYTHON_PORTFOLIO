# library
from math import factorial


# function
def fac(num, show):
    '''
    parameter num: Variable of type integer (int). It is the number to calc the factorial.
    parameter show: Variable of type string (str). It is the choice to show or not the calculation.
    return: Return the factorial of the variable.
    Function created by Marcus Padilha.
    '''
    if show == "N":
        return factorial(num)
    else:
        for count in range(num, 0, -1):
            if count == 1:
                print(f"{count} = ", end="")
            else:
                print(f"{count} x ", end="")
        return factorial(num)


# input
number = int(input("Enter the number to calc its factorial: "))
choice = input("Do you want see the calculation? [Y/N]").strip().upper()

# output
print(fac(number, choice))
