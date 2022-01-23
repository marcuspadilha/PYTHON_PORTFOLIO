distance = int(input("Input in kilometers the distance of the travel: "))
print(f"The price of the travel is $ {distance*0.5}." if distance<=200 else f"The price of the travel is $ {distance*0.45}.")