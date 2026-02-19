# Vamos criar um tradutor simples
# Ele vai receber uma palavra em inglês e retornar a tradução em português

from deep_translator import GoogleTranslator

texto = input("Digite uma palavra ou uma frase para ser traduzida: ")

tradução = GoogleTranslator(source='auto', target='pt').translate(texto)

print(f"A tradução de '{texto}' é: '{tradução}'")


