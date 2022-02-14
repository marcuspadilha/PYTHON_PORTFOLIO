# statements
student = dict()
setofgrades = list()
grade = 0


# library
from time import sleep
# function
def grades(lst, chc):
    student['total'] = len(lst)
    student['biggest'] = max(lst)
    student['smallest'] = min(lst)
    student['mean'] = round(sum(lst) / len(lst), 2)
    if chc == "Y":
        if student['mean'] < 5:
            student['situation'] = "Bad"
        elif 5 <= student['mean'] < 7:
            student['situation'] = "Reasonable"
        elif 7 <= student['mean'] <= 10:
            student['situation'] = "Good"
    return student


# input
while True:
    grade = float(input("\033[1;38mInput the student's grade: "))
    setofgrades.append(grade)
    choice1 = input("Do you want to continue? [Y/N]").strip().upper()
    if choice1 == "N":
        break
    grade = 0
    sleep(0.5)
sleep(0.5)
print()
choice2 = input("Do you want show the situation? [Y/N]").strip().upper()
print()
sleep(0.5)
# output
answer = grades(setofgrades, choice2)
print(answer)
input()