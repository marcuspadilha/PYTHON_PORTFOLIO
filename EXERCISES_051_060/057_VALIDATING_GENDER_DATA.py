# input
sex = input("Enter your sex: [M/F] ").strip().upper()
while sex != "M" and sex != "F":
    if sex != "M" or sex != "F":
        sex = input("Invalid data. Please enter your sex: [M/F] ").strip().upper()
#output
if sex == "M":
    print(f"\nSuccessfully registered male sex.")
if sex == "F":
    print(f"\nSuccessfully registered female sex.")
