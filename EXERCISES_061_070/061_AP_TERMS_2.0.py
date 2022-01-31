#input
term = int(input("Input the first term of the AP: "))
reason = int(input("Input the reason of the AP: "))
quantity = int(input("Enter how many terms of the AP: "))
#processing
while quantity>0:
    print(term, end=" ")
    term += reason
    quantity -= 1
input()