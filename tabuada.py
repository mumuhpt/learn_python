# Imprimindo a tabuada de um número
import os
num = int(input("Digite um número para ver sua tabuada: "))

while True:
    for i in range(1, 11):
        print(num, 'x', i, '=', num * i)

    continuar = input("Deseja ver a tabuada de outro número? (s/n): ")
    os.system('cls' ) #Limpa a tela do terminal, para ficar mais organizado.
    if continuar.lower() != 's':
        print("Encerrando o programa. Até mais!")
        break
    else:
        num = int(input("Digite um número para ver sua tabuada: "))








