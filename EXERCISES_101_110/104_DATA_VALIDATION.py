# library
def readint(ask):
    global number
    print(ask, end="")
    number = input()
    while True:
        if not number.isnumeric():
            print("\033[1;31mERROR! Type a valid integer number.")
            print(ask, end="")
            number = input()
        else:
            break
    return number


# main program
number = readint("\033[1;38mEnter a number: ")
print(f"\033[1;34mYou have just typed the number \033[1;33m{number}\033[1;38m.")
