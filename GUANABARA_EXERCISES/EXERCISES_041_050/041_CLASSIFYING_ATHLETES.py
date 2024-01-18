# statements


# library
import datetime
from datetime import date

# input
birthyear = int(input("Input the year of the birth: "))
atual = date.today().year

# processing
print(f"The athlete is {abs(birthyear - atual)} years old.")

if 0 <= abs(birthyear - atual) < 10:
    print("Classification : Child")

elif 10 <= abs(birthyear - atual) <= 14:
    print("Classification : Infant")

elif 14 < abs(birthyear - atual) <= 19:
    print("Classification : Junior")

elif 19 < abs(birthyear - atual) <= 25:
    print("Classification : Senior")

elif 25 < abs(birthyear - atual):
    print("Classification : Master")

else:
    print(f"ERROR! No such classification exists.")

input()