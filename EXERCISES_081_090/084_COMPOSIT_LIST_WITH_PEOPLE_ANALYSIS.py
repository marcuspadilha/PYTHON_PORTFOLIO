#statements
people = list()
data = list()
count = minweight = maxweight = 0
choice = str()
#input
while choice != "N":
    data.append(str(input("\033[1;38mInput person's name: ")))
    data.append(int(input("\033[1;38mInput person's weight in kg: ")))
    if len(people) == 0:
        minweight = maxweight = data[1]
    else:
        if data[1]>maxweight:
            maxweight = data[1]
        if data[1]<minweight:
            minweight = data[1]
    people.append(data[:])
    data.clear()
    choice = input("Do you want to continue: [Y/N]").strip().upper()


#output
print("\033[1;32m")
print(f"In the total you registered {len(people)} people")
print(f"\033[1;32mThe smallest weight was {minweight} kg and it was of: ", end="")
for parse in people:
    if minweight == parse[1]:
        print(parse[0], end= " ")
print("\033[1;32m")
print(f"The biggest weight was {maxweight} kg and it was of: ", end="")
for parse in people:
    if maxweight == parse[1]:
        print(parse[0], end= " ")