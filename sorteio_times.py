# Programa para sortear times de futebol e separalos em 4 grupos

import random
times = ['Atletico Mineiro', 'Flamengo', 'Atletico Paranaense',
        'Cruzeiro', 'Internacional', 'Bahia', 'Fortaleza',
        'Vitoria', 'Curitiba', 'Gremio', 'Sao Paulo', 'Avai',
        'Palmeiras', 'Santos', 'Corinthians', 'Vasco', 
        'Botafogo', 'Fluminense', 'Goias', 'Chapecoense'] # Lista de times com 20 times de futebol

random.shuffle(times) # Embaralha a lista de times
grupos = [[], [], [], []] # Cria uma lista de 4 grupos vazios

for i in range(len(times)):
    grupos[i % 4].append(times[i]) # % 4 garante que os grupos fiquem com quantidades iguais 
for i in range(4):
    print(f'Grupo {i + 1}: {grupos[i]}')
