# Vamos criar uma calculadora de juros compostos

print('Bem-Vindo a nossa Calculadora de Juros Compostos! ')
print('Vamos Calcular o seu investimento!')

capital_inicial = float(input('Digite o valor inicial do investimento: '))
taxa_juros = float(input('Digite a porcentagem de juros mensal: '))
taxa_juros_correta = taxa_juros / 100
# print(taxa_juros_correta)
tempo_aplicacao = int(input('Quantos meses o dinheiro será aplicado? '))

montante_final = capital_inicial * (1 + taxa_juros_correta) ** tempo_aplicacao
print(f'O valor final do seu investimento será: {montante_final}')


