#statements
count = numberchose = 0
numbers = list()
#input
while True:
    number = int(input("\033[1;38mEnter a number: "))
    numbers.append(number)
    count += 1
    choice = input("Do you want to continue? [Y/N] ").strip().upper()
    if choice == "N":
        break
numbers.sort(reverse=True)
numberchose = int(input("What number do you want see if it is in the list? "))
print("\033[1;34m")
print(f"You typed {count} elements.\n"
      f"\033[1;32mThe values typed in the inverse order is {numbers}")
if numberchose in numbers:
    print(f"\033[1;33mThe number {numberchose} is in the list.")
else:
    print(f"\033[1;31mThe number {numberchose} is not in the list.")