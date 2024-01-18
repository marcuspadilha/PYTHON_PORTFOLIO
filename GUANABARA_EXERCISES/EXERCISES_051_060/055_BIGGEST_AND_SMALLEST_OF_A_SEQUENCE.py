# library

#statements
sweight = 0
bweight = 0
# input
for p in range(1,6):
    weight = float(input(f"Input the {p}º person's weight: "))
# processing
    if p == 1:
        sweight = weight
        bweight = weight
    if weight < sweight:
        sweight = weight
    if weight > bweight:
        bweight = weight
#output
print(f"The biggest weight inputted was {bweight} and the smallest was {sweight}.")
input()