def increase(value=0, tax=0, formatted = False):
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
