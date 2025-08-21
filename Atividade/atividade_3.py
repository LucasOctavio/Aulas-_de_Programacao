#media de notas dos alunos
notas = []

while True:
    entrada = input("Digite uma nota ou 'sair' para ver a sua media: ")
    if entrada.lower() == "sair":
        break
    nota = float(entrada)
    if 0 <= nota <= 10:
        notas.append(nota)
    else:
        print("Nota inválida! Digite entre 0 e 10.")

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(f"Média do aluno: {media:.2f}")
    if media >= 7:
        print("Aluno Aprovado!")
    else:
        print("Aluno Reprovado!")
else:
    print("Nenhuma nota foi digitada.")