# Vemos verificar a senha do usuario se é forte, media ou fraca
# Senha deve conter, Numeros, Carach especiais e Letras maiusculas e minusculas
def verificar_senha(senha):
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False

    especiais = "!@#$%&*()_+-={}[]:;<>.,?/"

    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        if caractere.islower():
            tem_minuscula = True
        if caractere.isdigit():
            tem_numero = True
        if caractere in especiais:
            tem_especial = True

    pontos = 0

    if len(senha) >= 8:
        pontos += 1
    if tem_maiuscula:
        pontos += 1
    if tem_minuscula:
        pontos += 1
    if tem_numero:
        pontos += 1
    if tem_especial:
        pontos += 1

    if pontos <= 2:
        return "Senha fraca"
    elif pontos == 3 or pontos == 4:
        return "Senha média"
    else:
        return "Senha forte"


senha = input("Digite a senha: ")
print(verificar_senha(senha))