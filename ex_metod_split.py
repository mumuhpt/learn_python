
nome = input('Digite seu nome: ') # Recebo um input com nome, um com idade e um com salario
idade = input('Digite sua idade: ')
salario = input('Digite seu salário: ') 

arquivo = open('dados.txt', 'w') # Abro um arquivo para escrita 
arquivo.write(nome + ',' + idade + ',' + salario) # Armazeno os dados recebidos nos inputs acima, separados por vírgula
arquivo.close() # Fecho o arquivo para garantir que os dados sejam salvos corretamente

arquivo = open('dados.txt', 'r') # Abro o arquivo para leitura 
conteudo = arquivo.read() # Leio o que foi escrito no arquivo 
arquivo.close()

dados = conteudo.split(',') # Uso o método split para dividir a string em uma lista, usando a vírgula como separador.

print('Nome:', dados[0]) # Imprimo o nome, idade e salario na tela usando os índices da lista criada pelo split.
print('Idade:', dados[1])
print('Salário:', dados[2])

