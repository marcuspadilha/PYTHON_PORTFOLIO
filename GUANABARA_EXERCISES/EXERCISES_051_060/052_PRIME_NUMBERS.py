# input
number = int(input("Input the number to analyse: "))
count = 0
# processing

for c in range(1, number+1):
    if number % c == 0:
        count += 1
if count > 2:
    print(f"The number {number} is not a prime number.")
else:
    print(f"The number {number} is a prime number.")

input()

