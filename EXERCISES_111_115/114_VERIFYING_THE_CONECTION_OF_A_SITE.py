from urllib import request, error

# library
try:
    site = request.urlopen("https://www.pudim.com")
except error.URLError:
    print("\033[1:31mThe site is not accessible at the moment.\033[m")
else:
    print("\033[1:32mThe site is accessible.\033[m")

