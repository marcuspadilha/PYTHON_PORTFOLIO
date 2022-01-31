#statement
number = sum =  count = biggestnumber = smallestnumber = 0
option = "Y"

#procesing
while option != "N":
    number = int(input("Enter a number: "))
    count += 1
    if count == 1:
        biggestnumber = number
        smallestnumber = number
    else:
        if number > biggestnumber:
            biggestnumber = number
        elif number < smallestnumber:
            smallestnumber = number
    sum += number
    option = input("Do you want to continue? [Y/N]").strip().upper()

print(f"You've typed {count} numbers and the mean was {sum/count:.2f}.")
print(f"The biggest value was {biggestnumber} and the smallest value was {smallestnumber}.")
