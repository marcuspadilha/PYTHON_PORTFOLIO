# statements


# library
import datetime
from datetime import date

# input
birthyear = int(input("Input the year of the birth: "))
atual = date.today().year

# processing
print(f"The athlete is {abs(birthyear - atual)} years old.")

if abs(birthyear - atual) < 10:
    print("Classification : Child")
elif 10 =< abs(birthyear - atual) < 10:
    print("Classification : Child")
