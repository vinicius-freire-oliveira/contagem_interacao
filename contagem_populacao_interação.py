# Solicita ao usuário a população e a taxa de crescimento do país A
popA = int(input("População do país A: "))
while popA < 0:
    # Garante que a população seja um valor positivo
    popA = int(input("População do país deve ser maior que 0: "))
taxaA = float(input("Taxa de crescimento da cidade A: "))

# Solicita ao usuário a população e a taxa de crescimento do país B
popB = int(input("População do país B: "))
while popB < 0:
    # Garante que a população seja um valor positivo
    popB = int(input("População do país deve ser maior que 0: "))
taxaB = float(input("Taxa de crescimento da cidade B: "))

ano = 0
# Continua a calcular os anos até que a população do país A ultrapasse a população do país B
while popA < popB:
    ano += 1
    # Calcula a nova população do país A e B com base nas taxas de crescimento
    popA = int((1 + (taxaA / 100)) * popA)
    popB = int((1 + (taxaB / 100)) * popB)
    # Imprime a população de ambos os países para o ano atual
    print("\nAno %d:" % ano)
    print("População A: %d" % popA)
    print("População B: %d\n\n" % popB)

# Após o loop, imprime o ano em que a população do país A ultrapassa a população do país B
print("Ultrapassa no ano:", ano)
