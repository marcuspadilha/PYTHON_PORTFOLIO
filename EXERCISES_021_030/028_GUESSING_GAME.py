from time import sleep
from random import randint
print("Thinking in a number from 1 to 5.")
sleep(0.5)
print(".")
sleep(0.5)
print(".")
number1 = randint(1,5)
sleep(0.5)
print(".")
sleep(0.5)
print(".")
sleep(0.5)
print(".")
number2=int(input("I thought in a number. Can you guess what number it is? "))
if number1 == number2:
    print(f"Congratulations! I really thought in the {number2}.")
else:
    print(f"I'm sorry! I thought in the {number1}.")
input()

