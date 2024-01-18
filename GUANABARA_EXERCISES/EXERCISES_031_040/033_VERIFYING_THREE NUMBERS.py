number1 = int(input("Input the first number: "))
number2 = int(input("Input the second number: "))
number3 = int(input("Input the third number: "))

if number1 > number2 and number1 > number3:
    print(f"The number {number1} is the biggest number.")
else:
    if number2 > number1 and number2 > number3:
        print(f"The number {number2} is the biggest number.")
    else:
        if number3 > number1 and number3 > number2:
            print(f"The number {number3} is the biggest number.")

if number1 < number2 and number1 < number3:
    print(f"The number {number1} is the smallest number.")
else:
    if number2 < number1 and number2 < number3:
        print(f"The number {number2} is the smallest number.")
    else:
        if number3 < number1 and number3 < number2:
            print(f"The number {number3} is the smallest number.")


