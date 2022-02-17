def increase(value=0, tax=0):
    answer = value + (value * (tax / 100))
    return answer


def decrease(value=0, tax=0):
    answer = value - (value * (tax / 100))
    return answer


def double(value=0):
    answer = value * 2
    return answer


def half(value=0):
    answer = value / 2
    return answer


def currency(value=0, currency="R$"):
    return f"{currency} {value:.2f}".replace('.', ',')
