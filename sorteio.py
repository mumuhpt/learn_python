import random
import os
# Lista de nomes aleatórios
print('Essa é a rifa do Mumu!')
print('Boa sorte a todos os participantes!')

while True:
    
    num_usuario = input('Por favor, insira o numero de 1 a 100 de sua escolha: ')
    
    try:
        num_usuario = int(num_usuario)
        if num_usuario > 100:
            print('Número inválido. Por favor, insira um número menor ou igual a 100.')
            continue
    except ValueError:
        print('Entrada inválida. Por favor, insira um número válido.')
        continue

    nomes = [
        "Ana", "Bruno", "Carlos", "Diana", "Eduardo",
        "Fernanda", "Gabriel", "Helena", "Igor", "Juliana",
        "Kevin", "Laura", "Marcelo", "Nina", "Oscar",
        "Patricia", "Samuel", "Rafael", "Sandra", "Tiago",
        "Lucas", "Victor", "Wagner", "Ana Paula", "Yara",
        "Camila", "Adriano", "Beatriz", "Caio", "Camila",
        "Cristina", "Daniel", "Daniela", "David", "Milena",
        "Debora", "Diego", "Diogo", "Maristela", "Donato",
        "Dorival", "Douglas", "Judith", "Edmundo", "Elaine",
        "Elena", "Elias", "Marcelo", "Elisa", "Elisson",
        "Eliza", "Elizeu", "Elke", "Elmira", "Eloah",
        "Eloisa", "Elso", "Elton", "Elvira", "Elvis",
        "Elza", "Ema", "Emerson", "Emestina", "Emesto",
        "Emilia", "Emilio", "Emily", "Nina", "Emira",
        "Miranda", "Manuela", "Emma", "Emmanuel",
        "Isabela", "Abel", "Aline", "Ena", "Eneas",
        "Célia", "Eneida", "Thiago", "Nelson", "Enéas",
        "Enéias", "Enéo", "Eneri", 'Murilo', 'Andresa', 'Júlia'
        'Mariana', 'Sofia', 'Lara', 'Beatriz', 'Tereza', 'Clara', 
        'Vitória', 'Romeu', 'Davi', 'Heitor', 'Gael', 'Miguel', 'Bernardo',]

    nome_sorteado = random.randint(0, len(nomes) - 1)

    print(f'O nome sorteado foi: {nomes[nome_sorteado]}')

    if 0 <= int(num_usuario) < len(nomes):
        if nome_sorteado == int(num_usuario):
            print("\U0001F389 Parabéns! Você ganhou a rifa! \U0001F389")  # Party popper emoji

        else:
            print("\U0001F614 Que pena! Você não ganhou dessa vez. Tente novamente! \U0001F614")  # Pensive face emoji

        repetir = input('Deseja sortear outro nome? (s/n): ').strip().lower()
        os.system('cls')
        if repetir != 's':
            
            print('Encerrando o sorteio. Obrigado a todos!')
           
            break


