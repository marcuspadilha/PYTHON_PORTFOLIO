#statements
countleft = countright = 0
#input
expression = str(input("\033[1;38mEnter the expression to be parsed: "))
#processing
expression = list(expression)
for analyzer in expression:
    if analyzer == "(":
        countleft += 1
    elif analyzer == ")":
        countright +=1
#output
if countleft == countright:
    print("\033[1;33mThe expression is right!")
else:
    print("\033[1;31mThe expression is wrong!")