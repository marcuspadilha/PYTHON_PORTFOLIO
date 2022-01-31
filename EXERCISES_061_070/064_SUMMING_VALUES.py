#statement
number = 1
sum = 0
count = 0
#processing
while number != 0:
    number = int(input("Enter a number [0 to stop]: "))
    sum += number
    count += 1

print(f"You've typed {count-1} numbers and their sum is {sum}. ")
input()
