# library
import FUNCTIONS

# input
value = float(input("\033[1;38mEnter with the value: R$ "))
value = (FUNCTIONS.formating(value))
print()
print(FUNCTIONS.half(value))
print(FUNCTIONS.double(value))
print(FUNCTIONS.adding10(value))
input()