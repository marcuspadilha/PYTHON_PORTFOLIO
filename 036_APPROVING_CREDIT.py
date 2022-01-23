# input
value = int(input("Input the value of the home: $ "))
wage = int(input("Input the wage of the buyer: $ "))
time = int(input("Input the time of the loan: $ "))

# processing
time = time*12
loan = value / time

# output
if loan <= wage * 0.3:
    print(f"To pay a house of $ {float(value)} in {time/12} years, the loan is $ {loan:.2f}.")
    print("Fundind granted!")
else:
    print(f"To pay a house of $ {float(value)} in {time / 12} years, the loan is $ {loan:.2f}.")
    print("Fundind denied!")
input()
