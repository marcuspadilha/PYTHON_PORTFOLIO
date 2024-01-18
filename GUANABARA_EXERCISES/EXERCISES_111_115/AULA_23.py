try:
    a = int(input("Numerator: "))
    b = int(input("Denominator: "))
    r = a/b
except (ValueError, TypeError):
    print("We had a problem with the kind of data typed.")
except (ZeroDivisionError):
    print("It's not possible divide by zero.")
except (KeyboardInterrupt):
    print("The user did not enter with the data.")
else:
    print(f"The result is {r}.")
finally:
    print("Thank you very much.")