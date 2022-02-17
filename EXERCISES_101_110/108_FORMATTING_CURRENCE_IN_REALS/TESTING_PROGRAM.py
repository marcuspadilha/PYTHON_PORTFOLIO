# library
import CURRENCY

# input
number = float(input("Input the value: R$ "))
print(f"The half of {CURRENCY.currency(number)} is {CURRENCY.currency(CURRENCY.half(number))}.")
print(f"The double of {CURRENCY.currency(number)} is {CURRENCY.currency(CURRENCY.double(number))}.")
print(f"Adding 10% in {CURRENCY.currency(number)} we get {CURRENCY.currency(CURRENCY.increase(number,10))}.")