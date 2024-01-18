# function
def writer(sentence):
    print("~" * (len(sentence) + 10))
    print(f"    {sentence}")
    print("~" * (len(sentence) + 10))


# input
phrase = input("Input a phrase to be enhanced: ")

# output
writer(phrase)

input()