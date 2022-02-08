# function
def area(a,b):
    print(f"The area of a land of \033[1;34m{a} \033[1;38mx \033[1;34m{b} \033[1;38mis \033[1;33m{a*b} m².")

# enhancement
print("\033[1;38m-="*25)
print(f"{'Area of lands':^50}")
print("-="*25)
width = float(input("Input the land's width in meters: "))
length = float(input("Input the land's length in meters: "))
area(width, length)