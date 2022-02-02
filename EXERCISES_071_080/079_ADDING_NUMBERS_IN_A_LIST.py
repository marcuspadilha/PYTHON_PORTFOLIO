print("\033[1;38m","-="*30)
#statements
numbers = list()
#input
while True:
    number = int(input("Input a value: "))
    if number not in numbers:
        numbers.append(number)
        print("\033[1;33mValue added successfully.")
    else:
        print("\033[1;31mDuplicate value. Not added.")
    print("\033[1;38m")
    choice = input("Do you want to continue? [Y/N]").strip().upper()
    if choice == "N":
        break
print("\033[1;38m")
print("-="*30)
print(f"\033[1;34mYou typed the numbers {numbers}.")