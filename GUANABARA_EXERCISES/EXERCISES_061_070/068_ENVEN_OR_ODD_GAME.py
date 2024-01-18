#library
from random import randint

#enhancement
print("\033[1m", "@"*60, "\n", " "*17,"Let's play even or odd!", "\n", "@"*60)

#statements
uservalue = computervalue = count = 0
#input
while True:
    computervalue = randint(0,10)
    uservalue = int(input("\033[1;38mInput a value:"))
    choice = input("Do you want even or odd? [E/O] ").strip().upper()
    print(f"The computer played {computervalue}. ")
    if choice == "E":
        if (computervalue+uservalue)%2==0:
            print("\033[1;33m Congratulations, You WIN!!!")
            count += 1
        else:
            print("\033[1;31mYou LOSE!")
            break
    elif choice == "O":
        if (computervalue+uservalue)%2!=0:
            print("\033[1;33m Congratulations, You WIN!!!")
            count += 1
        else:
            print("\033[1;31mYou LOSE!")
            break
print(f"\033[1;34mGAME OVER! You have won {count} times.")
input()

