# input
grade1 = float(input("Input the first grade: "))
grade2 = float(input("Input the second grade: "))
grade3 = float(input("Input the third grade: "))
grade4 = float(input("Input the fourth grade: "))

# processing
average = (grade1+grade2+grade3+grade4)/4
if 0 <= average < 5:
    print(f"The student mean is {average} and he is REPROVED.")
elif 5 <= average < 7:
    print(f"The student mean is {average} and he is in RECUPERATION.")
elif 7 <= average <= 10:
    print(f"The student mean is {average} and he is APPROVED.")
else:
    print(f"ERROR! The mean {average} does not exist.")