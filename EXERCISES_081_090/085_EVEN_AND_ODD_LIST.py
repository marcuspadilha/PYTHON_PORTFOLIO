# statements
numbers = [[], []]
#input

for count in range(1,8):
    number = int(input(f"Input the {count}º value: "))
    if number%2 == 0:
        numbers[0].append(number)
        numbers[0].sort()
    else:
        numbers[1].append(number)
        numbers[1].sort()

print(f"The even typed values were: {numbers[0]}")
print(f"The odd typed values were: {numbers[1]}")