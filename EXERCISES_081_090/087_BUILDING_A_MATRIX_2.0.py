# statement
matrix = list()
line01 = list()
sum = int()
sum02 = int()
matrix = [[[], [], []], [[], [], []], [[], [], []]]
count = maxvalue = 0

for l in range(0, 3):
    for c in range(0,3):
        number = int(input(f"Input a number for [{l}{c}]: "))
        if number%2 == 0:
            sum += number
        if c == 2:
            sum02 += number
        if l == 1:
            count +=1
            if count == 1:
                maxvalue = number
            else:
                if maxvalue<number:
                    maxvalue = number



        matrix[l][c] = number
print("-=" * 30)
for count in range(0, 3):
    for count02 in range(0, 3):
        print(f"\033[1;32m[{matrix[count][count02]:^5}] ", end=" ")
    print(" ")
print(f"The sum of the even numbers is {sum}.")
print(f"The sum of the third colum is {sum02}.")
print(f"The biggest value of the second line is {maxvalue}.")


