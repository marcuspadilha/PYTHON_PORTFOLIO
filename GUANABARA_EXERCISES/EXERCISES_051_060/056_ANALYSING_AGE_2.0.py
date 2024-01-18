#statements
oldest = 0
sumages = 0
youngwomen = 0
# input
for c in range(1,5):
    print(f"------ {c}º Person -------")
    name = input("Input name: ")
    age = int(input("Input age: "))
    sex = input("Sex [M/F]: ").strip().upper()
# processing
    sumages = sumages+age
    if sex == "M" and age > oldest:
        oldest = age
        oldestman = name
    if sex == "F" and age < 20:
        youngwomen += 1

#otput
print(f"The average age of the group is {sumages/4:.2f} years old.")
print(f"The oldest man is {oldest} years old and his name is {oldestman}.")
print(f"Overall, there are {youngwomen} women below 20 year old. ")



