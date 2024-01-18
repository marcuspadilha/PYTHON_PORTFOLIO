# library
import CURRENCY

# input
number = float(input("Input the value: R$ "))
print(f"The half of {CURRENCY.currency(number)} is {CURRENCY.half(number, True)}.")
print(f"The double of {CURRENCY.currency(number)} is {CURRENCY.double(number, True)}.")
print(f"Adding 10% in {CURRENCY.currency(number)}, we get {CURRENCY.increase(number, 10, True)}.")
print(f"Decreasing 10% in {CURRENCY.currency(number)}, we get {CURRENCY.decrease(number, 10, True)}")