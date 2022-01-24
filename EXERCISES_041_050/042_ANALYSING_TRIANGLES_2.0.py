# input
line1 = int(input("Input the first line: "))
line2 = int(input("Input the second line: "))
line3 = int(input("Input the third line: "))

# processing
if line1 >= (line2+line3) or line2 >= (line1+line3) or line3 >= (line1+line2):
    print("The three lines cannot form a triangle.")
else:
    if line1 == line2 or line1 == line3 or line2 == line3:
        print("The three lines can form a isosceles triangle.")
    else:
        print("The three lines can form a scalene triangle.")

input()
