print('Calculadora de IMC')

nome = input('Digite o seu nome: ')
altura = float(input('Digite a sua altura em metros: '))
peso = float(input('Digite o seu peso em quilos: '))

imc = peso / altura ** 2

print(nome, 'tem', altura, 'de altura e pesa', peso, 'quilos e seu IMC é', f'{imc:.2f}')

if imc < 18.5:
    print('Você está abaixo do peso ideal.')
    print('Você deve ganhar peso para alcançar o peso ideal.')
elif imc < 25:
    print('Você está com o peso ideal.')
    print('Continue mantendo um estilo de vida saudável para manter o peso ideal.')
elif imc < 30:
    print('Você está com sobrepeso.')
    print('Você deve perder peso para alcançar o peso ideal.')
elif imc < 35:
    print('Você está com obesidade grau 1.')
    print('Você deve perder peso para alcançar o peso ideal e reduzir os riscos à saúde associados à obesidade.')
elif imc < 40:
    print('Você está com obesidade grau 2.')
    print('Você deve perder peso para alcançar o peso ideal e reduzir os riscos à saúde associados à obesidade.')
else:    
    print('Você está com obesidade grau 3.')
    print('Você deve perder peso para alcançar o peso ideal e reduzir os riscos à saúde associados à obesidade.')

