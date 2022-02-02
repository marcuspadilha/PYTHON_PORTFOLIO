# input
word01 = input("Input the first word: ").strip().upper()
word02 = input("Input the second word: ").strip().upper()
word03 = input("Input the third word: ").strip().upper()
word04 = input("Input the fourth word: ").strip().upper()
word05 = input("Input the fifth word: ").strip().upper()
#processing
words = (word01, word02, word03, word04, word05)
for count in range(0, len(words)):
    print(f"In the word {words[count]} there are the vowels: ", end=" ")
    word = tuple(words[count])
    for count2 in word:
        if count2 == "A":
            print("a",end=" ")
        elif count2 == "E":
            print("e",end=" ")
        elif count2 == "I":
            print("i",end=" ")
        elif count2 == "O":
            print("o",end=" ")
        elif count2 == "U":
            print("u",end=" ")
    print("\033[m")