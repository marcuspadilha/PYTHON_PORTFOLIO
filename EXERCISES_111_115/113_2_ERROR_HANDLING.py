# function
def readint(num):
    while True:
        try:
            number = int(input(num))
        except (ValueError, TypeError):
            print("\033[1;31mERROR! Type a valid numer\33[1;38m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[1;31mEntrance of data interrupted by the user.\33[1;38m")
            break
        else:
            return number


def readfloat(num):
    while True:
        try:
            number = float(input(num))
        except (ValueError, TypeError):
            print("\033[1;31mERROR! Type a valid numer\33[1;38m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[1;31mEntrance of data interrupted by the user.\33[1;38m")
            break
        else:
            return number



# input
numberint = readint("\33[1;38mEnter a value: ")
numberfloat = readfloat("Enter a real number: ")
if numberint != None and numberfloat != None:
    print(f"The typed values were {numberint} and {numberfloat}.")