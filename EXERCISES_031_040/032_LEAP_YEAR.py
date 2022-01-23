year = int(input("Input a year to verify if it is leap: "))
if year%400==0:
    print(f"The year {year} is a leap year.")
else:
    if year%100==0:
        print(f"The year {year} is not a leap year.")
    else:
        if year%4==0:
            print(f"The year {year} is a leap year.")
        else:
            print(f"The year {year} is not a leap year.")


