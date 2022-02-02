#enhancements
print("\033[1;38m","%"*60)
print(f"{'CASH MACHINE':^56}")
print("","%"*60)
#input
value = int(input("How many do you want withdraw? $ "))
#processing
total =value
note = 50
totalnotes = 0

while True:
    if value >= note:
        value -= note
        totalnotes+=1
    else:
        if totalnotes>0:
            print(f"Total of \033[1;34m {totalnotes} \033[1;38m notes of\033[1;33m $ {note}\033[1;38m.")
        if note == 50:
            note = 20
        elif note == 20:
            note = 10
        elif note == 10:
            note = 1
        totalnotes = 0
        if value == 0:
            break

input()