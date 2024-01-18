# enhancement
print("\033[1;43;38m~~" * 30)
print(f"{'PYTHON HELP SYSTEM':^55}")
print("\033[1;43;38m~~" * 30)


def aid(fct):
    print("\33[1;44;38m~~" * 30)
    print(f"{f'Accessing the {fct} manual command.':^55}")
    print("\33[1;44;38m~~" * 30)

    print(f"\33[1;7;48;30m")
    print(help(fct))

while True:
    choice = input("\033[m\033[1;38mEnter Function or Library: ")
    aid(choice)
    choice = input("\033[m\033[1;38mDo you want to continue? [Y/N] ").strip().upper()
    if choice == "N":
        break
    print()
input()
