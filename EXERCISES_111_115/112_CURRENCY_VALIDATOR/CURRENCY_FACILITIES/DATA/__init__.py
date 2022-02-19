def validator(num):
    valid = False
    while valid == False:
        entrance = str(input(num)).replace(",",".")
        if entrance.isalpha() == True or entrance.strip() == "":
            print(f"ERROR! \"{entrance}\" is not a valid value.")
        else:
            valid = True
            return float(entrance)