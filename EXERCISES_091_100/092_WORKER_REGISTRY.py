#library
from datetime import datetime
# statement
data = dict()

# input
data['name'] = input("\033[1;38mEnter the name: ").strip().capitalize()
data['birthyear'] = int(input("Enter the birth's year: "))
data['worksnumber'] = int(input("Enter the work card number (0 if not): "))
if data['worksnumber'] > 0:
    data['hireyear'] = int(input("Enter the year of hire: "))
    data['wage'] = float(input("Enter the wage: $ "))
    data['retirement'] = (datetime.now().year) - (data['birthyear']) + ((data['hireyear']+35)-datetime.now().year)
# output
print("-="*30)
print(f"The worker's name is {data['name']}")
print(f"{data['name']}'s age is {(datetime.now().year) - (data['birthyear'])}")
if data['worksnumber'] <= 0:
    print(f"{data['name']} never worked.")
else:
    print(f"{data['name']}'s work card number is {data['worksnumber']}")
    print(f"{data['name']}'s wage is: $ {data['wage']}")
    print(f"{data['name']} will retire being {data['retirement']}")