# library
from CURRENCY_FACILITIES import CURRENCY
from CURRENCY_FACILITIES import DATA

# input
number = DATA.validator("\033[1;38mInput the value: R$ ")
print()
CURRENCY.summary(number, 20, 12)
input()