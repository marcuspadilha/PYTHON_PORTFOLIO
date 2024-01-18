
# input
price = float(input("Input the purchase price: $ "))
print('''\nMethods of payment:
[1] In cash
[2] In sight on the card
[3] 2x in the card
[4] 3x or more in the card\n''')
method = int(input("What is the method of payment? "))

# processing
if method == 1:
    print(f"The purchase of $ {price} is going to cost $ {price*0.9}.")
elif method == 2:
    print(f"The purchase of $ {price} is going to cost $ {price*0.95}.")
elif method == 3:
    print(f"The purchase is going to cost $ {price} in 2 times of $ {price/2}.")
elif method == 4:
    times = int(input("How many times in the card? "))
    if times > 10:
        print("The maximum amount of installments is 10 times.")
    elif 3 <= times <= 10:
        print(f"The purchase of $ {price} is going to cost $ {price * 1.2} in {times} times of $ {(price*1.2)/times}.")
    else:
        print(f"ERROR! No such option exists.")
else:
    print("ERROR! No such option exists.")
input()

