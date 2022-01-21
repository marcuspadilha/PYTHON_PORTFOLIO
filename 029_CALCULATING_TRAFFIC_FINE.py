from random import randint
from time import sleep
print("Reading the car's speed.")
sleep(0.5)
print(".")
sleep(0.5)
speed = randint(30,130)
print(".")
sleep(0.5)
print(".")
print(f"Speed : {speed} Km/h.")
if speed > 80:
    print(f"The car exceeded the speed limit. The fine is $ {(speed-80)*7:.2f}.")
else:
    print("The car is inside the speed limit.")
input()