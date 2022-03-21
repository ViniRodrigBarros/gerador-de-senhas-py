#Gerador de senhas
import random
import string
opção=0
opção2=0
tamanho=0
nome=''
senha=""

def senha_gerador(tamanho):
    options = string.ascii_letters + string.digits
    maiuscula = "ABCDEFGHIJKMNOPQRSTUVWXYZ"
    Minuscula = "abcdefghijkmnopqrstuvwxyz"
    numero = string.digits
    caracteres_especiais="!@#$%&*"
    senha=""
    digit1 = random.choice(maiuscula)
    digit2 = random.choice(Minuscula)
    digit3 = random.choice(numero)
    digit4 = random.choice(caracteres_especiais)
    senha = digit1 + digit2 + digit3 + digit4
    for i in range(3,tamanho):
        digit5=random.choice(options)
        senha = senha + digit5
    return senha
while True:
    print("Selecione a opção: ")
    print("[1] - criar senha :")
    print("[2] - Visualizar senhas :")
    print("[-1] - Sair.")
    opção = int(input())
    if opção == -1:
        break
    if opção == 2:
        with open('senhas11.txt', 'r') as arquivo:
            for valor in arquivo:
                print(valor)
    if opção == 1:
        print("informe o nome da senha")
        nome=str(input())
        print("Informe o tamanho da senha com no minimo 4 digitos ")
        tamanho = int(input())
        senha_gerada=senha_gerador(tamanho)
        print("Senha gerada:")
        print(nome)
        print(senha_gerada)
        print('')
        print("[1] - salvar senha  :")
        print("[2] - menu")
        opção2=int(input())
        if opção2 == 1:
            with open('senhas11.txt', 'a') as arquivo:
                for valor in nome:
                    arquivo.write(str(valor))
                arquivo.write("\n")
                for valor in senha_gerada:
                    arquivo.write(str(valor))
                arquivo.write("\n")
            print("Senha salva")
        else:
            continue