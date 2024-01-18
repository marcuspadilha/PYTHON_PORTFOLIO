wage = float(input("Input the wage in dollars: "))
print(f"The new wage is $ {wage*1.1}." if wage>1250 else f"The new wage is $ {wage*1.15}.")