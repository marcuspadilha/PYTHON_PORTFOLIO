# libraries
from time import sleep

# statements
option = 0

# inputs
print("Welcome I'm the new calculator.")

while option != 5:
    option = 0
    number01 = int(input("Input the first value: "))
    number02 = int(input("Input the second value: "))
    while option != 4 and option != 5:
        print("\nSelect an option:")
        print("[1] Sum\n"
              "[2] Multiply\n"
              "[3] Biggest\n"
              "[4] New numbers\n"
              "[5] Run out of the program.\n")
        option = int(input("Enter your option: "))
        if option == 1:
            print(f"{number01} + {number02} = {number01+number02}")
            input("For new options, press enter key.")
        elif option == 2:
            print(f"{number01} x {number02} = {number01*number02}")
            input("For new options, press enter key.")
        elif option == 3:
            if number01 > number02:
                print(f"The number {number01} is the bigger.\n")
                input("For new options, press enter key.")
            elif number01 < number02:
                print(f"The number {number02} is the bigger.\n")
                input("For new options, press enter key.")
            else:
                print("The two numbers are equal.\n")
                input("For new options, press enter key.")
        elif option == 4:
            print("\n")
        elif option != 5:
            print("Invalid option. Try again.\n")
            input("For new options, press enter key.")


print("Ending")
sleep(2)
print("End of the program.")
input()