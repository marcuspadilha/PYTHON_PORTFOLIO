# library
from datetime import date

#statements

year = date.today().year
legalage = 0
underade = 0

# input
for n in range(1, 8):
    age = int(input(f"In which year the {n}ª person was born? "))
    if year - age >= 18:
        legalage += 1
    else:
        underade += 1

# output
print(f"\nIn the total there was {legalage} people of legal age, and {underade} underage people.")

