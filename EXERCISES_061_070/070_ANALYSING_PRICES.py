# enhancements
print("\033[1;38m", "%" * 60, "\n", " " * 18, "REGISTER OF PRODUCTS", "\n", "%" * 60)
# statements
price = sum = plus1000 = count = smallestprice = 0
smallestproduct = productname = "A"
# processing
while True:
    productname = input("\033[1;37mEnter the product's name: ")
    price = float(input("\033[1;37mEnter the product's price: $ "))
    sum += price
    count += 1
    if price > 1000:
        plus1000 += 1
    if count == 1:
        smallestprice = price
        smallestproduct = productname
    else:
        if price < smallestprice:
            smallestprice = price
            smallestproduct = productname
    choice = input("Do you want to continue? [Y/N] ").strip().upper()
    if choice == "N":
        break
    print("\n")
print("\n")
print(f"\033[1;34mThe total of buying is $ {sum}.")
print(f"\033[1;34mThere are {plus1000} products costing more than $ 1000,00.")
print(f"\033[1;34mThe cheapest product is the {smallestproduct} that costs $ {smallestprice}. ")
