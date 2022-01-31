# statement
term01 = 0
term02 = 1
term03 = 1

# input
terms = int(input("Enter how many terms you want show: "))

# processing
print(f"{term01} {term02}", end=" ")
while (terms - 2) > 0:
    print(term03, end=" ")
    terms -= 1
    term01 = term02
    term02 = term03
    term03 = term01 + term02
input()

