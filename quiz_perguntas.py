# Vamos criar um programa de quiz de perguntas e respostas
# O programa deve mostrar uma pergunta e 4 opções de resposta
# O programa deve permitir que o usuário escolha uma opção
# O programa deve mostrar se a resposta está correta ou incorreta
# O programa deve mostrar a pontuação final do usuário
import os 
import time

perguntas = [
    {   
        'pergunta': 'Qual é a capital da França?',
        'opcoes': ['A-) - Paris', 'B-) - Londres', 'C-) - Roma', 'D-) - Berlim'],
        'resposta': 'A'
    
    },
    {
        'pergunta': 'Qual é a capital da Itália?',
        'opcoes': ['A-) - Paris', 'B-) - Londres', 'C-) - Roma', 'D-) - Berlim'],
        'resposta': 'C'
    },
    {
        'pergunta': 'Qual é a capital da Alemanha?',
        'opcoes': ['A-) - Paris', 'B-) - Londres', 'C-) - Roma', 'D-) - Berlim'],
        'resposta': 'D'
    }
]

pontuacao = 0

for index, perguntas in enumerate(perguntas):
    os.system('cls')

    print('-------------------------------')
    print(f'------Pergunta {index + 1} de {len(perguntas)}----------')
    print(f'\n {perguntas['pergunta']}\n')
    
    for opcao in perguntas['opcoes']:
        print(opcao)

    resposta_usuario = input('\nDigite a letra da sua resposta: ').strip().upper()
    if resposta_usuario == perguntas['resposta']:
        print('\nResposta correta!')
        pontuacao += 1
    else:
        print('\nResposta incorreta! A resposta correta é:', perguntas['resposta'])

    time.sleep(2)

os.system('cls')
print('================================')
print('Quiz finalizado!')
print(f'Sua pontuação final é: {pontuacao} de {len(perguntas)}')
print('Obrigado por jogar!')
print('================================')

