
import random
import os

while True:

    print('Jogo do Pedra Papel e Tesoura! ')

    escolha = input(str('Escolha, Pedra, Papel ou Tesoura: '))

    print()

    escolha_jogador = escolha.lower()

    print(f'Você escolheu, {escolha_jogador}.') 

    ppt = ['pedra', 'papel', 'tesoura']
   
    ppt_sorteado = random.choice(ppt)

    print(f'O programa escolheu, {ppt_sorteado}.')

    if escolha_jogador == ppt_sorteado:

        print('As duas escolhas são iguais, resultado: Empate.')

    elif escolha_jogador == 'pedra' and ppt_sorteado == 'tesoura':

        print('Parabéns você venceu!')

    elif escolha_jogador == 'tesoura' and ppt_sorteado == 'pedra':

        print('Infelizmente você perdeu!')

    elif escolha_jogador == 'papel' and ppt_sorteado == 'pedra':

        print('Parabéns você venceu!')

    elif escolha_jogador == 'pedra' and ppt_sorteado == 'papel':

        print('Infelizmente você perdeu!')

    elif escolha_jogador == 'tesoura' and ppt_sorteado == 'papel':

        print('Parabéns você venceu!')

    elif escolha_jogador == 'papel' and ppt_sorteado == 'tesoura':

        print('Infelizmente você perdeu!')
    print()
    print('Deseja jogar novamente? ')

    reiniciar = input('Sim ou não: ')
    sim = True
    não = False
    os.system('cls')
    if reiniciar == 'não':

        break

