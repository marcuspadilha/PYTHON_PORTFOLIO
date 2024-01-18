from random import randint
number = int(input("\033[1;38mHow many games do you want draw? "))
print("-+"*30)
for count in range(1,number+1):
    draws = [randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60)]
    print(f"\033[1;38mgame {count}: \033[1;33m{draws}")
print("\033[1;38m-+"*30)