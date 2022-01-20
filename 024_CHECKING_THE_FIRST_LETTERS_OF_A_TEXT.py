city = input("Input the name of the city: ").strip().upper()
city = city.split()
if city[0] == "SANTO":
    print("The name of the city starts with Santo.")
else:
    print("The name of the city does not start with Santo.")
input()