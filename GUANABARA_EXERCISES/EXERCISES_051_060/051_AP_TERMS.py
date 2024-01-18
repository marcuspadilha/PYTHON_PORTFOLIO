# input
first = int(input(("Input the first term of the AP: ")))
term = int(input("Input the term of the AP: "))
quantity = int(input("Input the quantity os terms in that AP: "))
last = first+(quantity-1)*term
# processing
#print("\n")
for c in range(first, last + 1, term):
    print(c, end=" → ")
print("It's over.")
input()