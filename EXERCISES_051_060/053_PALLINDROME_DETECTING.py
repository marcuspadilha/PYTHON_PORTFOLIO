# input
phrase = input("Input the phrase to analyse: ").strip().upper()

# processing
word = phrase.split()
together = "".join(word)
inverse = ""
for letter in range(len(together)-1,-1,-1):
    inverse += together[letter]
if inverse == together:
    print(f"The inverse of {together} is {inverse}. Thus, the phrase is a palindrome.")
else:
    print(f"The inverse of {together} is {inverse}. Thus, the phrase is not a palindrome.")