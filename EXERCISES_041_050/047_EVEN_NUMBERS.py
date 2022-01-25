# statements


# library


# input
number1 = int(input("Input the first number: "))
number2 = int(input("Input the last number: "))
# processing
if number1%2 == 0:
    for c in range(number1,number2+1,2):
        print(c)
else:
    for c in range(number1+1,number2+1,2):
        print(c)
# output
