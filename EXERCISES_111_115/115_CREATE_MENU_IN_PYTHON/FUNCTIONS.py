def options():
    print("\033[1;38m-" * 40)
    print(f"{'MAIN MENU':^40}")
    print("-" * 40)
    print("\033[1;33m1 - \033[1;34m See registered people.")
    print("\033[1;33m2 - \033[1;34m Register new person.")
    print("\033[1;33m3 - \033[1;34m Exit the system.")
    print("\033[1;38m-" * 40)


def enter():
    people = list()
    person = dict()
    num = 0
    while True:
        options()
        try:
            number = int(input("\033[1;33mEnter with your option: \033[1;38m"))
        except (ValueError, TypeError):
            print("\033[1;31mERROR! Please, type a valid number.\33[1;38m")
        except (KeyboardInterrupt):
            print("\n\033[1;31mEntrance of data interrupted by the user.\33[1;38m")
            break
        else:
            if number < 1 or number > 3:
                print("\033[1;31mERROR! Please, type a valid option.\33[1;38m")
            elif number == 1:
                print("\033[1;38m-" * 40)
                print(f"{'REGISTERED PEOPLE':^40}")
                print("-" * 40)
                for count in people:
                    print(f"\033[1;37m{count['name']:<20}{count['age'] :>10} years old\033[1;38m")
                print()

            elif number == 2:
                person['name'] = input("Enter the person's name: ")
                person['age'] = input("Enter the person's age: ")
                people.append(person.copy())
                num += 1

            elif number == 3:
                print("\033[1;38m-" * 40)
                print(f"{'Exiting the system.':^40}")
                print("-" * 40)
                break
