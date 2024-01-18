# library
from FUNCTIONS import enter
from FILES import *
# files
file = "register.txt"
if not fileexist(file):
    createfile(file)
# function
enter(file)
