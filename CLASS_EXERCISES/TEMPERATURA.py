temperatura = int(input("Informe a temperatura atual: "))

if temperatura > 30:
    print("Está quente hoje! Beba bastante água. \U0001F975")
elif temperatura > 20:
    print("Dia agradável! Vamos aproveitar. \U0001F60E")
elif temperatura > 10:
    print("Está um pouco frio. Que tal um casaco? \U0001F9E5")
else:
    print("Brrr! Está muito frio! Melhor ficar em casa.\U0001F976")

