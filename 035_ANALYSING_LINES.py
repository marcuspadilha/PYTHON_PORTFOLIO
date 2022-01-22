line1 = int(input("Input the first line: "))
line2 = int(input("Input the second line: "))
line3 = int(input("Input the third line: "))

if line1 >= (line2+line3):
    print("The three lines cannot form a triangle.")
else:
    if line2 >= (line3 + line1):
        print("The three lines cannot form a triangle.")
    else:
        if line3 >= (line2 + line1):
            print("The three lines cannot form a triangle.")
        else:
            print("The three lines can form a triangle.")