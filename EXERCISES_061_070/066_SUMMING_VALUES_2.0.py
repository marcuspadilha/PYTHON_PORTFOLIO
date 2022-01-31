#statement
value = sum = count = 0
#processing
while True:
    value = int(input("Type a value (-1 to stop): "))
    if value == -1:
        break
    sum += value
    count += 1
print(f"The sum of the {count} valous is {sum}.")
input()