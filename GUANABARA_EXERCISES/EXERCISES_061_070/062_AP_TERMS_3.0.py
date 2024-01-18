#input
term = int(input("Enter the first term of the AP: "))
reason = int(input("Enter the reason of the AP: "))
quantity = int(input("Enter how many terms of the AP: "))
#statements
quantityterms = 0
#processing
while quantity > 0:
    while quantity>0:
        print(term, end= " ")
        quantityterms += 1
        term += reason
        quantity -= 1
    quantity = int(input("\nHow many terms do you want show more? "))
print(f"AP finalized with {quantityterms} terms showed.")
input()