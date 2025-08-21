#atividade de numeros em orden crescente
numeros = []

while True:
    entrada = input("Digite um número (ou 'sair' para terminar): ")
    if entrada.lower() == "sair":
        break
    numeros.append(int(entrada))

numeros.sort()
print("Números em ordem crescente:", numeros)
