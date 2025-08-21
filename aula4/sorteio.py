'''
    programa: sorteio V.1.0
    importanndo biblioteca
    aula 04: 19/08/2025
    '''

    #importando biblioteca (lib)

import random
def sorteio():
    nome1 = input('digite o primeiro nome')
    nome2 = input('digite o segundo nome')
    nome3 = input('digite o terceirp nome')
    nome4 = input('digite o quarto nome')
    nome5 = input('digite o quinto nome')

    lista_de_nomes = [nome1, nome2, nome3, nome4, nome5]

    escolhido = random.choice(lista_de_nomes)
    print(escolhido)

def sorteio2():
    lista = []
    sair = False
    while sair  == False:
        nome_candidato = input('digite os nomes para o sorteio ou aperte enter para sair: ')
        if nome_candidato !="":
            lista.append(nome_candidato)
        else:
            sair =True
    escolhido = random.choice(list)
    print('o escolhodo foi: ',escolhido)

def sorteio3():
    import random
    import time
    import os

    lista_nomes = []
    lista_sorteio  = []

    while True:
        nome = input('digite o nome para o sorteio: ')
        if nome:
            lista_nomes.append(nome)
        else:
            break
    while True:
        if lista_nomes:
            os.system('cls')
            escolhido = random.choice(lista_nomes)   #sorteoa um nome na lista de nomes
            lista_sorteio.append(escolhido)             #adiciona ele na lista
                         #remove ele da lista (ele pega o primeiro que ele encontrr)

            if escolhido in lista_nomes():
                del[escolhido]
                lista_nomes.remove(escolhido)
                print('nome excluido')
                print(lista_nomes)


            print(f'O escolhido foi: {escolhido}')
            opcao = input('deseja sortear outros nome?\n S - sim \n| N - não\n').lower()
            os.system('cls')

            if opcao == 'S':
                break
            else:
                print('Não a nomes para serem sorteados!  ')
                break
                print('programa  Finlizado')
                print(f'os sortedos foram: {lista_sorteio}')


'''
pop - função, remove pelo indice - remmove indices peimarios ou novos

    pop() - remove o ultimo indice
    pop(0) - remove o indice 0

del - instrução, remove item pelo inddice com quantidades, mais de 1 item
 del[3] - vai buscar pelo indice 3
del[2:10] - vai reover os indices do 2 ao 10
del[escolhido]

remove - remove a partirde uma variavel
    lista.remove(variavel)
'''


def sorteio4():
    from random import randint
    from os import system
    from time import sleep as tempo


    print('tente adivinhar o numero! ')
    num1 = int(input('Digite um numero:'))
    num_secreto = randint(1,100)
    if num1 == num_secreto:
        print('parabens você venceu o jogo')
    else:
        print('Você errou o numero era:')
        system('cls')

def Sorteio5():
    import random
    from os import system
    from time import sleep as tempo
    max_tentativas = 10
    acertou = False

    max = int(input("digite: "))
    numero_secreto = random.randint(1,max)
    print(30*'-','bem vindo ao tigrinho',30*'-')
    tentativa= 0
    print('Voçê tem: ', max_tentativas,'tentativas de adivinhar')
    print('vamos começar?')

    while tentativa < max_tentativas:
        try:
            palpite = int(input('digite o seu palpite: '))
        except ValueError:
            print('Por favor, digite umm numero')
            continue
        tentativa += 1

        #verificar palpite
        if palpite == numero_secreto:
            acertou = True
            break

        elif palpite < numero_secreto:
            print('tente un número maior! ')
            tempo(2)
            system('cls')
        elif palpite > numero_secreto:
            print('Tente um número menor ')
            tempo(2)
            system('cls')

'''
del(nome_lista[posição])deleeta uma possição espesifica
#ValueError                                  #  Exeção de valor - correção de erro



separador = ","

nome_string = separador.join(nomes_lista)


mese_string = [janeiro fevereiro março abril maio junho]
messe_lista = messes_string.spli('')

for mes in messe_list
print(mes)

somar
numeros =[1,2,3,4,5,6,7,8,9,10]
print(sum(numeros))

nummeros.sort(re)
'''
Sorteio5()