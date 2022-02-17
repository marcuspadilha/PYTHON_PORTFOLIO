def increase(value=0, tax=0, formatted = False):
    answer = value + (value * (tax / 100))
    return answer if formatted is False else currency(answer)


def decrease(value=0, tax=0, formatted = False):
    answer = value - (value * (tax / 100))
    return answer if formatted is False else currency(answer)


def double(value=0, formatted = False):
    answer = value * 2
    return answer if formatted is False else currency(answer)


def half(value=0, formatted = False):
    answer = value / 2
    return answer if formatted is False else currency(answer)


def currency(value=0, currency="R$"):
    return f"{currency} {value:.2f}".replace('.', ',')
