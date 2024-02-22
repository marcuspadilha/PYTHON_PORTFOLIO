texto = "exemplo de texto exemplo de análise, em um exemplo de análise racional"

palavras = texto.split()

print(palavras)

frequencia = {}

for palavra in palavras:

    if palavra in frequencia:
        frequencia[palavra] += 1

    else:
        frequencia[palavra] = 1

for palavra, freq in frequencia.items():

    print(f"{palavra}: {freq}")


