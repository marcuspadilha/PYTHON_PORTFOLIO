# statements
numberswritten = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                  "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
                  "nineteen", "twenty")
#input
while True:
    number = int(input("Type a number from 0 to 20: "))
    print(f"You typed the number {numberswritten[number]}.")

input()