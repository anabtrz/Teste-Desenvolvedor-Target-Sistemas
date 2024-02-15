palavraParaInverter = input("Digite uma string: ")
palavraInvertida = ""
i = len(palavraParaInverter) - 1

while i >= 0:
    palavraInvertida += palavraParaInverter[i]
    i -= 1

print("A palavra digitada invertida fica " + palavraInvertida)