# enhancement
print("\033[1;38m", "%" * 60)
numbers = list()
# input
for count in range(0, 10):
    value = int(input("\033[1;38mEnter a value: "))
    if count == 0 or value > numbers[len(numbers) - 1]:
        numbers.append(value)
        print("\033[1;33mIt was added in the final of the list...")
    else:
        position = 0
        while position < len(numbers):
            if value <= numbers[position]:
                numbers.insert(position, value)
                break
            position += 1
        print(f"\033[1;33mIt was added in the {position + 1}ª position.")
#output
print("\033[1;34m")
print(f"The values typed in order were {numbers}")
