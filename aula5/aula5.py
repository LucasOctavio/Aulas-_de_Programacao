def Calculadora_d_gasolina():
    while True:
        try:
            etanol = float(input('Digite o preço do Etanol: ').replace(',','.'))
            gasolina =float(input('Digite o Valor da Gasolina: ').replace(',','.'))
            calculo = (etanol/gasolina*100)
            resultado = "gasolina" if calculo >= 70 else 'Etanol'
            print(f'Resultado = {calculo:.2f}%. compensa abastecer com {resultado}')
            opcao = input('Deseja refazer o calculo? (s/n)').lower().strip()   # ele remove os espaços a mais
            match opcao:                                            # Usa-se o match case quando já se sabe qual é o valor
                case 's':
                    continue
                case 'n':
                    break
                case _:                                             # Exeção, no caso o else
                    print(f'Opção invalida!')
                    continue
        except Exception as e:
            print(f'Não foi possivel iniciar a operação. {e}')
            continue


#================================================ Crud ==========================================
# Mainpulação de Arquivos
# Leitura de arquivos
def crud():
    with open('texto.txt', 'r', encoding='utf-8') as file:     # with open - abre um aquivo | ('texto.txt') - fala qual é o arquivo a ser aberto | 'r' fala qual a função
        texto = file.read()
    print(texto)

def teste1():
    import os
    while True:
        try:
            arquivo = input('Digite o nome do arquivo sem extenção:').lower().strip()
            with open(f'{arquivo}.txt', 'r', encoding='utf-8') as f:
                arquivo_aberto = f.read()
                os.system('cls' if os.name == 'nt' else 'clear')

            print(arquivo_aberto)

            while True:
                 prosseguir = input('Deseja abrir outro arquivo? (s/n): ').lower().strip()
                 if prosseguir == 's' or prosseguir == 'n':
                     break
                 else:
                     print('Opção invalida!')
                     continue
            match prosseguir:
                 case 's':
                     continue
                 case 'n':
                     break
        except Exception as e:
            print(f'Não foi possivel ler o arquivo. Erro {e}')
            continue



def Atividade3():
    import os
    while True:
        try:
            novo_texto = input('Digite o texto: \n')
            nome_arquivo = input('Digite o nome do arquivo (sem extenção): ').strip().lower()

            with open(fr'C:\git\logica_de_programacao_aulas\aula_5\{nome_arquivo}.txt', 'w', encoding='utf-8') as f:      # O 'w' substitiu os arquivos dentro
                f.write(novo_texto)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'{nome_arquivo}.txt gravado com sucesso.')

            while True:
                 prosseguir = input('Deseja abrir outro arquivo? (s/n): ').lower().strip()
                 if prosseguir == 's' or prosseguir == 'n':
                     break

                 else:
                     print('Opção invalida!')
                     continue

            match prosseguir:
                 case 's':
                     continue
                 case 'n':
                     break

        except Exception as e:
            print(f'Não foi possivel ler o arquivo. Erro {e}')
            continue

def Atividade4():
    import os

    while True:
        try:
            novo_texto = input('Digite o texto: ')
            nome_arquivo = input('Digite o nome do arquivo (sem extensão .txt): ').strip().lower()

            with open(fr'(suapasta){nome_arquivo}.txt', 'w', encoding='utf-8') as f:
                f.write(novo_texto)

            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'{nome_arquivo}.txt gravado com sucesso')


            while True:
                prosseguir = input("Deseja continuar? (s/n): ").strip().lower()
                if prosseguir == 's' or prosseguir == 'n':
                    break
                else:
                    print("Opção inválida.")

            match prosseguir:
                case 'n':
                    break
        except Exception as e:
            print(f"Erro ao gravar o arquivo: {e}")
            continue


def Atividade5():
    import os
    while True:
        try:
            nome_arquivo = input('Digite o nome do arquivo (sem extenção): ').strip().lower()
            novo_texto_adicionar = input('Digite o novo texto:\n')

            with open(fr'C:\git\logica_de_programacao_aulas\aula_5\{nome_arquivo}.txt', 'a', encoding='utf-8') as f: # O 'a' adiciona ao arquivo
                f.write(f'\n{novo_texto_adicionar}')
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Gravado com sucesso.')

            with open(f'{nome_arquivo}.txt', 'r', encoding='uft-8') as f:
                texto_final = f.read()                                      # Fazer a leitura do arquivo que etá dnetro de f
            print(f'Texto final: {texto_final}')

            while True:
                 prosseguir = input('Deseja abrir outro arquivo? (s/n): ').lower().strip()
                 if prosseguir == 's' or prosseguir == 'n':
                     break

                 else:
                     print('Opção invalida!')
                     continue

            match prosseguir:
                 case 's':
                     continue
                 case 'n':
                     break

        except Exception as e:
            print(f'Não foi possivel ler o arquivo. Erro {e}')

def Atividade6():
    import json
    try:
        arquivo = input('Digite o nome do arquivo: ').strip().lower()
        with open(f'{arquivo}.json', 'r', encoding='utf-8')
            dados = json.load()
        print(f'{'-'*20} DADOS {'-'*20}\n')
        for dado in dados:
            for chave in dado:
                print(f'{chave.capitalize} : {dado.get(chave)}')
            print(f'{chave.capitalize()} : {dado.get(chave)}')
            print(40*'-')
    except Exception as e:
        print(f'Não foi possivel lerr o arquivo. Erro {e}')

Atividade6()