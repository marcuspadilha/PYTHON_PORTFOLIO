# statement
person = dict()
people = list()
count = sumage = 0
# input
while True:
    while True:
        person['name'] = input("Enter with person's name: ").strip().capitalize()
        if person['name'].isalpha() == False:
            print("ERROR! Please, type a real name!")
        else:
            break


    while True:
        person['sex'] = input(f"Enter with {person['name']}'s sex: [M/F]").strip().upper()
        if person['sex'] not in ["M", "F"]:
            print("ERROR! Please, answer only M or F.")
        else:
            break

    while True:
        person['age'] = input(f"Input {person['name']}'s age: ").strip()

        if person['age'].isnumeric() == False:
            print("ERROR! Please, type a real age!")
        else:
            person['age'] = int(person['age'])
            sumage += person['age']
            break

    while True:
        choice = input("Do you want to continue? [Y/N]").strip().upper()
        if choice not in ['Y','N']:
            print("ERROR! Please, answer only Y or N.")
        else:
            if choice == "Y":
                print("-="*60)
                break
            elif choice == "N":
                break
    count += 1
    people.append(person.copy())
    if choice == "N":
        break
print("-="*60)
mean = sumage/count
print(f"A) In the total, {count} people were registered.")
print(f"B) The mean of the ages is {mean} years old.")
print(f"List of people with age above the mean: ")





