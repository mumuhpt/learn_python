# criando um gerador de keys ou senhas aleatorias 

import random, string, os

while True:
    carach = string.ascii_letters + string.punctuation + string.digits

    key = "".join(random.choices(carach, k=24))

    print(f'Sua Key de acesso é: {key}')
    print('Deseja gerar outra Key?')
    
    escolha = input('Digite (s) para sim e (n) para não. ')

    if escolha != "s":
        break
    else:
        os.system('cls')
        continue

          

    

    
    

