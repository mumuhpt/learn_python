print('Calculadora de Gasto calórico médio basal.')
# Calculo do gasto calórico médio basal usando a fórmula de Mifflin-St Jeor
# Formula essa que é atualmente considerada a mais precisa para calcular o gasto calórico médio basal.
print('Por favor, informe os seguintes dados para calcular o seu gasto calórico médio basal:')

nome = input('Digite o seu nome: ')
sexo = input('Digite o seu sexo (M para masculino, F para feminino): ')
if sexo.upper() not in ['M', 'F']:
    print('Sexo inválido. Por favor, informe M para masculino ou F para feminino.')
else:
    idade = int(input('Digite a sua idade em anos: '))
    peso = float(input('Digite o seu peso em quilos: '))
    altura = float(input('Digite a sua altura em centímetros: '))
    print()


    if sexo.upper() == 'M':
        gasto_calorico =  (10 * peso) + (6.25 * altura) - (5 * idade) - 5
   
        print(nome, 'tem', idade, 'anos de idade, pesa', peso, 'quilos, tem', altura, 'cm de altura \n' \
        'e seu gasto calórico médio basal é', f'{gasto_calorico:.2f}', 'calorias por dia.')

    elif sexo.upper() == 'F':
        gasto_calorico =  (10 * peso) + (6.25 * altura) - (5 * idade) - 161
   
        print(nome, 'tem', idade, 'anos de idade, pesa', peso, 'quilos, tem', altura, 'cm de altura \n' \
        'e seu gasto calórico médio basal é', f'{gasto_calorico:.2f}', 'calorias por dia.')

    
        
    
    