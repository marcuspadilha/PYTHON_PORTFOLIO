# input
number = int(input("Input an integer number: "))
print("Choose an option of base to conversion: \n[1] To BINARY \n[2] To OCTAL \n[3] To HEXADECIMAL.")
option = int(input("Your option: "))

# processing
if option == 1:
    binary=bin(number)
    print(f"{number} converted to BINARY is {binary[2:]}.")
elif option == 2:
    octal = oct(number)
    print(f"{number} converted to OCTAL is {octal[2:]}.")
elif option == 3:
    hexadecimal = hex(number)
    print(f"{number} converted to HEXADECIMAL is {hexadecimal[2:]}.")
else:
    print("ERROR! There's no such option.")
input()
