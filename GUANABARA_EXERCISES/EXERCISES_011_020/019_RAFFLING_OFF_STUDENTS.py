from random import choice
sdt1 = input("Input the first student's name: ")
sdt2 = input("Input the second student's name: ")
sdt3 = input("Input the third student's name: ")
sdt4 = input("Input the forth student's name: ")
list = [sdt1,sdt2,sdt3,sdt4]
print(f"The selected student is {choice(list)}.")
input()