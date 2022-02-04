#statements
studentdata=dict()
geraldata = list()
count = 0
#input
while True:
    studentdata['Name'] = str(input("Enter the student's name: "))
    studentdata['grade01']= float(input("Enter the student's first grade: "))
    studentdata['grade02'] = float(input("Enter the student's second grade: "))
    studentdata['Mean'] = (studentdata['grade01']+studentdata['grade02'])/2
    count += 1
    geraldata.append(studentdata.copy())
    choice = input("Do you want to continue? [Y/N]").strip().upper()
    if choice == "N":
        break
#output
print("=-"*30)
print(f"{'Nº':<3} {'NAME':<16} {'MEAN':<8}")
print("-"*30)
for c in range(0,count):
    print(f"{c:<3} {geraldata[c]['Name']:<16} {geraldata[c]['Mean']:<8.2f}")
print("=-"*30)
while True:
    choicestudent = int(input("Show the grades of which student? (-1 to interrupt) "))
    print(f"The grades of {geraldata[choicestudent]['Name']} are {geraldata[choicestudent]['grade01'], geraldata[choicestudent]['grade02']}. ")
    choice = input("Do you want to continue? [Y/N]").strip().upper()
    print("=-" * 30)
    if choice == "N":
        break
input()
