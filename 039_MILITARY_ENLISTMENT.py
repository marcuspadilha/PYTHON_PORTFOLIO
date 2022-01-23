# library
from datetime import date

# input
birth = int(input("Input the year of birth: "))
atual = date.today().year

# processing
if (abs(birth-atual)==18):
    print(f"You are {abs(birth-atual)} years old in {atual}.\n You have to enlist immediately. ")
elif (abs(abs(birth-atual)<18)):
    print(f"You are {abs(birth-atual)} years old in {atual}.\n Your enlistment will be in {birth+18-atual} years.")
else:
    print(f"You are {abs(birth - atual)} years old in {atual}.\n Your enlistment was supposed to be"
          f" {atual-(birth + 18)} years ago.")

input()