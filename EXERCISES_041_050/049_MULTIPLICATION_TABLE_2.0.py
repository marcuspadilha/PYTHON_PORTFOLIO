# input
number = float(input("input the number to be the multiplicand: "))
number01 = int(input("input the number to be the first multiplier : "))
number02 = int(input("input the number to be the last multiplier : "))
# processing
for c in range(number01,number02+1):
    print(f"{number} x {c} = {number*c:.2f}")
