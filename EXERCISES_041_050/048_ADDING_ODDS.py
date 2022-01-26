#statements
sum = 0
c = 0
count = 0
# input
number1 = int(input("Input the first number: "))
number2 = int(input("Input the last number: "))
# processing
for c in range(number1, number2 + 1):
    if c % 3 == 0:
        if c % 2 != 0 :
            sum = sum + c
            count += 1


print(f"\nThe of the {count} values multiples by 3 and odds between the range {number1} and {number2} is {sum}.")
