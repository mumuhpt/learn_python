# Criando um programa para cadastrar os alunos e calcular a média de cada um deles.
# O programa deve solicitar o nome do aluno e as notas de cada uma das provas que ele fez.
# O programa deve salvar os dados dos alunos em um arquivo de texto e calcular a média de cada um deles.

print('Vamos cadastrar os alunos e calcular a média de cada um deles.')
print('Cada aluno deve ser cadastrado com o nome e a nota de cada uma das provas que ele fez.')
print('Maximo de 20 alunos para cadastro.')

max_alunos = 20
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

with open('alunos.txt', 'w') as arquivo:
    while True:
        total_alunos = int(input('Quantos alunos deseja cadastrar? '))
        if total_alunos > max_alunos or total_alunos <= 0:
            print(f'Número de alunos inválido. Maximo de {max_alunos} alunos. Tente novamente.')
            continue
        
        for i in range(total_alunos):
            nome = input(f'Nome do aluno {i + 1}: ')
            nota1 = float(input(f'Nota da prova 1 do aluno {nome}: '))
            nota2 = float(input(f'Nota da prova 2 do aluno {nome}: '))
            print(f'Notas do aluno {nome} cadastradas com sucesso!')
            print('Calculando a média do aluno...')
            media = calcular_media(nota1, nota2)

            print(f'Aluno {nome} tem a média de {calcular_media(nota1, nota2):.2f}.')
            if media >= 7:
                print(f'O aluno {nome} foi aprovado!')
            elif media >= 5:
                print(f'O aluno {nome} está de recuperação!')
            else:
                print(f'O aluno {nome} foi reprovado!')    
            print()
            arquivo.write(f'O Aluno {nome} tem as notas {nota1} e {nota2} e media de {media:.2f}\n')
        print('Alunos cadastrados com sucesso!')
        break

        
