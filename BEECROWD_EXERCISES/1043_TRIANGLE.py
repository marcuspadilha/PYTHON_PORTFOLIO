A = float(input())
B = float(input())
C = float(input())

if A+B>C and A+C>B and B+C>A:
    print(f"Perimetro = {A+B+C}")
else:
    print(f"Area = {((A+B)*C/2)}")