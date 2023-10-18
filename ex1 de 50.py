import random
import string
a = 0
b = 0
senhas = []
letras_min = "abcdefghijklmnopqrstuvwxyz"
letras_mai = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
carac = "@&#*$%¨<>"

print("A senha irá conter: 9 digitos, letras maiusculas, letras minusculas, numeros e caracteres especiais.\n")
qtde = int(input("Digite a quantidade de senhas que deseja gerar?: "))

while b < qtde:
    senha = []
    for a in range(9):
        if a == 0 or a == 4:
            senha.append(str(random.randint(0, 9)))
        elif a == 1 or a == 5 or a == 8:
            senha.append(random.choice(letras_min))
        elif a == 2 or a == 6:
            senha.append(random.choice(letras_mai))
        else:
            senha.append(random.choice(carac))
    random.shuffle(senha)
    senha_str = ''.join(senha)
    senhas.append(senha_str)
    b += 1
for i, senha in enumerate(senhas):
    print(f"Senha {i + 1}: {senha}")
