# statement
studentgrade = dict()
# input
studentgrade['name'] = input("Student's name: ")
studentgrade['mean'] = float(input(f"{studentgrade['name']}'s mean: "))
# processing
if studentgrade['mean'] >= 7:
    situation = "Approved"
elif 5 <= studentgrade['mean'] < 7:
    situation = "Recuperation"
elif studentgrade['mean'] <5:
    situation = "Reproved"
#output
print(f"The student's name is {studentgrade['name']}.")
print(f"The mean is {studentgrade['mean']}.")
print(f"The situation is {situation}.")