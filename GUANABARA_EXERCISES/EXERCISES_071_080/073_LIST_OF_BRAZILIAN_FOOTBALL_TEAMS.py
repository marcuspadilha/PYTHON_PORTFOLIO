#output
print("\033[1;38m")

print("-=" * 30)

print("Ranking of the soccer teams on the brazilian championship:\033[1;37m")
teams = ("Atlético-MG", "Flamengo", "Palmeiras", "Fortaleza", "Corinthians", "Bragantino", "Fluminense","América-MG", "Atlético-GO", "Santos","Ceará", "Internacional", "São Paulo", "Athletico-PR","Cuiabá", "Juventude", "Grêmio", "Bahia", "Sport", "Chapecoense")
print(teams)

print("\033[1;38m-="*30)

print("The top five are:\033[1;33m")
print(teams[:6])

print("\033[1;38m-="*30)

print("The last ones are:\033[1;31m")
print(teams[-5:])

print("\033[1;38m-="*30)

print("The teams in alphabetical order are:\033[1;32m")
print(sorted(teams))

print("\033[1;38m-="*30)

choice = input("What team do you want to ses the position? ").strip().capitalize()
for team in teams:
    if choice == team:
        print(f"\033[1;35m"
              f"The team {team} is in {teams.index(team)+1}º position.")

input()