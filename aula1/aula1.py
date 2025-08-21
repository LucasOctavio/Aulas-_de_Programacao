'''
print("Olá mundo, esse é o meu \nprimeiro script em \n python")
print(40*"-","concatenando texto",40*"-")
nome = "gomes"
altura="1.7"

print("Nome: ",nome)
ativo = True

print(type(ativo))
print()
print(30*"-","operações",30*"-")
#oprerações
num1=10
num2=10
expo=num1**num2
soma=num1+num2
divi=num1/num2
mult=num1*num2
sub=num1-num2
resto=num1%2
divisao_inteira=num1//num2
print("Resutado da soma", num1,"+",num2,"é",soma)
print("Resutado da diisão", num1,"/",num2,"é",divi)
print("Resutado da subitração", num1,"-",num2,"é",sub)
print("Resutado da multiplicação", num1,"*",num2,"é",mult)
print("Resutado do esponencial",expo)
print("Resutado do esponencial",divisao_inteira)

print()
print(30*"-","operadores de comparação",30*"-")
#operadores de comparação
num1>num2
num1<num2
num1==num2
num1>=num2
num1<=num2
num1!=num2

ano=2025
print("ano atual",ano)
ano+=1
print('amo acrecido de +1',ano)
ano-=1
print('amo acrecido de -1',ano)
'''
#operadores logicos
#AND, OR, NOT
print(30*"-","Entrada de dados",30*"-")
nome_usuaro=input("digite o seu nome")
print("Seja bem vindo ao sistema python",nome_usuaro)

print()
print(30*"-","convertendo tipos de dados",30*"-")

ano_nascimento=input("digite seu ano de nascimento ")
print(type(ano_nascimento))
#convertendo para inteiro
ano_nascimento=int(ano_nascimento)
print(type(ano_nascimento))


n1=10
n2=20

print("a soma é: ", n1+n2, type(n1), float(n2))