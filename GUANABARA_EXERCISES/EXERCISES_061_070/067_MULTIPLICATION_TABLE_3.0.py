#input
while True:
    number = float(input("Input the number to multiply (0 to exit): "))
    if number == 0:
        break
    start = int(input("Input the first number to be the multiplier: "))
    end = int(input("Input the last number to be the multiplier: "))

    for c in range(start,end+1):
        print(f"{c} x {number} = {c*number:.2f}")

print("Application ended.")
input()