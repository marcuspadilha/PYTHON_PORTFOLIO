'''def increase(value=0, tax=0, formatted = False):
    """
    :param value: It is the value that the user chose for the variable number in the TESTING_PROGRAM.
    :param tax: It is the tax of increase. It is fixed in 10%.
    :param formatted: It is to define if the return will be formatted(True) or not(False).
    :return: It is the result which will be returned to the program TESTING_PROGRAM.
    """
    answer = value + (value * (tax / 100))
    return answer if formatted is False else currency(answer)


def decrease(value=0, tax=0, formatted = False):
    """
    :param value: It is the value that the user chose for the variable number in the TESTING_PROGRAM.
    :param tax: It is the tax of decrease. It is fixed in 10%.
    :param formatted: It is to define if the return will be formatted(True) or not(False).
    :return: It is the result which will be returned to the program TESTING_PROGRAM.
    """
    answer = value - (value * (tax / 100))
    return answer if formatted is False else currency(answer)


def double(value=0, formatted = False):
    """


    """
    answer = value * 2
    return answer if formatted is False else currency(answer)


def half(value=0, formatted = False):
    """
    :param value: It is the value that the user chose for the variable number in the TESTING_PROGRAM.
    :param formatted: It is to define if the return will be formatted(True) or not(False).
    :return: It is the result which will be returned to the program TESTING_PROGRAM.
    """
    answer = value / 2
    return answer if formatted is False else currency(answer)


def currency(value=0, currency="R$"):
    """
    :param value: It is the value that the user chose for the variable number in the TESTING_PROGRAM.
    :param currency: It is the kind of currency used in the program. It is fixed in Brazilians Reals (R$).
    :return: It is the value formatted in Brazilian Reals (R$).
    """
    return f"{currency} {value:.2f}".replace('.', ',')

print(f"The half of {CURRENCY.currency(number)} is {CURRENCY.half(number, True)}.")
print(f"The double of {CURRENCY.currency(number)} is {CURRENCY.double(number, True)}.")
print(f"Adding 10% in {CURRENCY.currency(number)}, we get {CURRENCY.increase(number, 10, True)}.")
print(f"Decreasing 10% in {CURRENCY.currency(number)}, we get {CURRENCY.decrease(number, 10, True)}")'''

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