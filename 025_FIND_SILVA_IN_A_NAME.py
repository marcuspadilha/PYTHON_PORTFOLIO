name = input("Input a name: ").strip().upper()
name=name.find("SILVA")
if name == -1:
    print("The name has no Silva in it.")
else:
    print("The name has Silva in it.")
input()