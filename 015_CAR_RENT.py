days = int(input("How many days the car was rented for? "))
km = int(input("How many kilometers did the car travel? " ))
print(f"For the rent of the car, the price to pay is $ {days*60+km*0.15:.2f}")