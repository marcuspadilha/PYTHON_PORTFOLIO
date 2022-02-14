# function
def vote(num):
    from datetime import date
    currentyear = date.today().year
    if (currentyear - number) < 16:
        return f"Being {currentyear-number}, the person does not vote."
    elif 16 <= (currentyear - number) < 18:
        return f"Being {currentyear - number}, the vote is optional."
    elif 18 <= (currentyear - number) < 60:
        return f"Being {currentyear - number}, the vote is mandatory."
    else:
        return f"Being {currentyear - number}, the vote is optional."

# input
number = int(input("\033[1;38mEnter birth year: "))
print(vote(number))
input()