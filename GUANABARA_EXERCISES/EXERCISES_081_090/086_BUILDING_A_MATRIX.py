# statement
matrix = [[[], [], []], [[], [], []], [[], [], []]]

# input
for count in range(0, 3):
    for count02 in range(0, 3):
        number = int(input(f"\033[1;38mInput a value for [{count}{count02}]: "))
        matrix[count][count02] = number
# processing
print("-=" * 30)
for count in range(0, 3):
    for count02 in range(0, 3):
        print(f"\033[1;32m[{matrix[count][count02]:^5}] ", end=" ")

    print(" ")
