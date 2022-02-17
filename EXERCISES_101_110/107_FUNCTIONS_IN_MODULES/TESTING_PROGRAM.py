# library
import CURRENCY

# input
number = float(input("Input the value: $ "))
print(f"The half of $ {number} is $ {CURRENCY.half(number)}.")
print(f"The double of $ {number} is $ {CURRENCY.double(number)}.")
print(f"Adding 10%, we get {CURRENCY.increase(number,10)}.")