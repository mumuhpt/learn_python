# Criando um programa para uma doceria
# O programa deve mostrar o cardapio
# O programa deve mostrar o preço de cada item
# O programa deve permitir que o cliente faça um pedido
# O programa deve calcular o total do pedido

# Criando o cardápio

cardapio = [
    "bolo de Cenoura",
    "bolo de Leite ninho",
    "pudim",
    "brigadeiro",
    "beijinho",
    "balha italiana" ]

precos = [
    20.00,  
    25.00,
    15.00,
    5.00,
    5.00,
    10.00
]


print('Bem vindo a doceria do Mumu!')
print('Aqui está o nosso cardápio:')
print('-----------------------------')
for i in range(len(cardapio)):
    print(f'{i+1} - {cardapio[i]} - R${precos[i]:.2f}')
print('-----------------------------')
# Fazendo o pedido
pedido = []
while True:
    item = int(input('Digite o número do item que deseja pedir (0 para finalizar): '))
    if item == 0:
        break
    elif item < 0 or item > len(cardapio):
        print('Item inválido, tente novamente.')
    else:
        pedido.append(item - 1)
# Calculando o total do pedido
total = 0
print('Seu pedido é esse:')
for i in pedido:
    print(f'- {cardapio[i]} - R${precos[i]:.2f}')
    total += precos[i]
print(f'Total: R${total:.2f}')
print('Obrigado por pedir na doceria do Mumu!')


