phrase = input("Input phrase to be analysed: ").strip().upper()
print(f"The letter A shows up {phrase.count('A')} times.")
print(f"The first letter A is in the {phrase.find('A')+1}ª position.")
print(f"The last letter A is in the {phrase.rfind('A')+1}ª position.")