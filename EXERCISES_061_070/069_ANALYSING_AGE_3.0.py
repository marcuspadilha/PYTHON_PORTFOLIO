#statement
man = youngwomen = plus18 = 0

#processing
while True:
   print("\033[1;38m","="*30,"\n"," "*5, "Register a person","\n", "="*30)
   age = int(input("Age: "))
   sex = input("Sex: [M/F] ").strip().upper()
   if age > 17:
      plus18 =+ 1
   if sex == "M":
      man += 1
   if sex == "F":
      if age < 20:
         youngwomen += 1

   choice = input("\033[1;37mDo you want continue: [Y/N] ").strip().upper()
   if choice == "N":
      break

print(f"\033[1;34mTotal of people in leagal age: {plus18}")
print(f"\033[1;34mIn the total, we have {man} men registered.")
print(f"\033[1;34mThere are {youngwomen} women below 20.")