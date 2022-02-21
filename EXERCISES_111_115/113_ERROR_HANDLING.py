# library
def readint(ask):
    print(ask, end="")
    number = input()
    while True:
        if not number.isnumeric():
            print("\033[1;31mERROR! Type a valid integer number.")
            print(ask, end="")
            number = input()
        elif number.isspace():
            print("\033[1;31mERROR! Type a valid integer number.")
            print(ask, end="")
            number = input()
        else:
            break
    return number


def readfloat(ask):
    print(ask, end="")
    number = input()
    while True:
        if number.isascii() and not number.isnumeric() and not number.isspace() and not number.isalpha() and not number.isalnum() and not None:
            break
        elif None:
            print("\033[1;31mERROR! Type a valid integer number.")
            print(ask, end="")
            number = input()
        else:
            print("\033[1;31mERROR! Type a valid integer number.")
            print(ask, end="")
            number = input()
    return number


# main program
numberint = readint("\033[1;38mEnter a integer number: ")
numberfloat = readfloat("\033[1;38mEnter a float number: ")

print(
    f"\033[1;34mYou have just typed the numbers \033[1;33m{numberint}\033[1;34m "
    f"and \033[1;33m{numberfloat}\033[1;34m.")
input()


'''def readfloat(ask):
    print(ask, end="")
    number = input()
    while True:
        if number.isspace():
            print("\033[1;31mERROR! Type a valid integer number.")
            print(ask, end="")
            number = input()
        elif number.isalpha():
            print("\033[1;31mERROR! Type a valid integer number.")
            print(ask, end="")
            number = input()
        elif number.isfloat():
            print("\033[1;31mERROR! Type a valid integer number.")
            print(ask, end="")
            number = input()
        elif not number.isnumeric() and number.isascii():
            break
        elif is jus
        else:
            print("\033[1;31mERROR! Type a valid float number.")
            print(ask, end="")
            number = input()
    return number'''