#statement
count = times09 = position03 = 0
#input
print("\033[1;38m")
number01 = int(input("Enter a number from 0 to 9: "))
number02 = int(input("Enter another number from 0 to 9: "))
number03 = int(input("Enter more another number from 0 to 9: "))
number04 = int(input("Enter the last number from 0 to 9: "))
#processing
numbers = (number01,number02,number03,number04)
print(f"You typed the numbers {numbers}.")
for count in numbers:
    if count == 9:
        times09 += 1
    if count == 3:
        position03 = numbers.index(count)+1
#output
print(f"The value 9 showed up {times09} times.")
if position03 == 0:
    print("The value 3 was not typed.")
else:
    print(f"The value 3 was typed in the {position03}ª position.")
print("The even values typed were:", end=" ")
for count in numbers:
    if count%2 == 0:
        print(count, end=" ")
print(".")