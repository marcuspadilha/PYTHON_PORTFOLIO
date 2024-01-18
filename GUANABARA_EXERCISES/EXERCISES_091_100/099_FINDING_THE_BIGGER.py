# library
from time import sleep

# statements
numbers = list()
# function
def bigger(lst):
    print("-=" * 20)
    print("\033[1;34mExamining the values entered: ")
    sleep(0.6)
    print(f"\033[1;38mA) The values are \033[1;33m", end=" ")
    for count in lst:
        print(count, end= " ")
    print("\033[1;38m.")
    sleep(0.6)
    print(f"B) It was typed \033[1;33m{len(lst)} \033[1;38mvalues.")
    sleep(0.6)
    print(f"C) The biggest value is \033[1;33m{max(lst)}\033[1;38m.")


# input
while True:
    number = int(input("\033[1;38mInput a number: "))
    numbers.append(number)
    choice = input("Do you want to continue? ").strip().upper()
    if choice == "N":
        break

bigger(numbers)
input()

