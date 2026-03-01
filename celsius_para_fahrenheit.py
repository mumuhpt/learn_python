# vamos criar um programa que conver a temperatura de celsius para fahrenheit e visse versa

print('\n Corversor de temperaturas')
print('Escolha a opção que deseja converter')

opcao = input('Digite 1 para converte Celcius para Fahrenheit ou 2 para converter Fahrenheit para celsius: ')

if opcao == '1':
    celsius = float(input('Digite a Temperatura em celsius para ser cenvertida: '))
    fahrenheit = celsius * 9/5 + 32

    print(f'A conversão de {celsius} C para Fahrenheit é {fahrenheit}')

else:
    fahrenheit = float(input('Digite a Temperatura em Fahrenheit para ser convertida: '))
    celsius = (fahrenheit - 32) * 5/9 # Verificar a formula

    print(f'A conversao de {fahrenheit} F para Celsius é {celsius}')

print()
print('Obrigado pos utilizar nosso programa')
    
