def increase(value, tax):
    answer = value + (value * (tax / 100))
    return answer


def decrease(value, tax):
    answer = value - (value * (tax / 100))
    return answer


def double(value):
    answer = value * 2
    return answer


def half(value):
    answer = value / 2
    return answer
