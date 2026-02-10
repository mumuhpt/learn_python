# Exemplo do Livro "Entendendo Algoritmos" - Capítulo 1
# Onde o autor explica sobre busca linear e busca binária
# Podemos ver com o exemplo dado de que a busca binária é mais eficiente do que a busca linear

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = [1, 3, 5, 7, 9]
print(pesquisa_binaria(minha_lista, 3))  
print(pesquisa_binaria(minha_lista, -1)) 

