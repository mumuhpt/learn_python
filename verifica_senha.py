import string

def validar_senha(senha):
    if len(senha) < 8:
        print("Senha deve ter pelo menos 8 caracteres")
    if not any(c.isupper() for c in senha):
        print("Senha deve ter letra maiúscula")
    if not any(c.isdigit() for c in senha):
        print("Senha deve ter número")
    if not any(c in string.punctuation for c in senha):
        print("Senha deve ter caractere especial")

senha = input("Digite a senha: ")
validar_senha(senha)