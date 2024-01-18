def currency(value=0, currency="R$"):
    """
    :param value: It is the value that the user chose for the variable number in the TESTING_PROGRAM.
    :param currency: It is the kind of currency used in the program. It is fixed in Brazilians Reals (R$).
    :return: It is the value formatted in Brazilian Reals (R$).
    """
    return f"{currency} {value:.2f}".replace('.', ',')

def summary(value,inc,dec):
    increase = value + (value * (inc / 100))
    decrease = value - (value*(dec/100))
    double = value * 2
    half = value / 2

    print("-"*30)
    print(f"{f'Summary of the Value':^30}")
    print("-"*30)
    print(f"{f'Parsed Value:':<20}{currency(value):>10}")
    print(f"{f'Double of the Value:':<20}{currency(double):>10}")
    print(f"{f'Half of the Value:':<20}{currency(half):>10}")
    print(f"{f'20% of increase:':<20}{currency(increase):>10}")
    print(f"{f'12% of decrease:':<20}{currency(decrease):>10}")
    print("-" * 30)