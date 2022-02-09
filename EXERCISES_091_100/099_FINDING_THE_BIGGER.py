# library
from time import sleep

# statements
numbers = list()
# function
def bigger(lst):
    print("-=" * 20)
    print("Examining the values entered: ")
    print(f"A) The values are ", end=" ")
    for count in lst:
        print(count, end= " ")
    print(".")
    print(f"B) It was typed {len(lst)} values.")
    print(f"C) The biggest value is {max(lst)}.")


# input
while True:
    number = int(input("Input a number: "))
    numbers.append(number)
    choice = input("Do you want to continue? ").strip().upper()
    if choice == "N":
        break

bigger(numbers)

