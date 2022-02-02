#statements
count = number = maxposition = minposition = min = max = count02 =0
numbers = list()
#input
for count in range(1,6):
    number = int(input(f"Enter a value for the position {count}: "))
    numbers.append(number)
    if count == 1:
        min = number
        max = number
    else:
        if min > number:
            min = number
        if max < number:
            max = number
for position, count in enumerate(numbers):
    count02 += 1
    if min == count:
        minposition = position
    if max == count:
        maxposition = position

#output
print(f"You typed the values: {numbers}")
print(f"The biggest value is {max} and it is in the {maxposition+1}ª position.")
print(f"The smallest value is {min} and it is in the {minposition+1}ª position.")