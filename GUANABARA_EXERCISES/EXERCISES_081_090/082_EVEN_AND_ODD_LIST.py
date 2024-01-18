# statements
numbers = list()
numberseven = list()
numbersodd = list()
number = count = 0
# input
while True:
    number = int(input("\033[38;1mEnter a number: "))
    numbers.append(number)
    choice = input("Do you want continue? [Y/N]").strip().upper()
    if choice == "N":
        break
# processing
for count in numbers:
    if count % 2 == 0:
        numberseven.append(count)
    else:
        numbersodd.append(count)
# output
print("-=" * 30)
print(f"\033[33;1mYou typed the numbers {numbers}")
print(f"\033[32;1mThe even numbers typed are {numberseven}.")
print(f"\033[34;1mThe odd numbers typed are {numbersodd}.")
