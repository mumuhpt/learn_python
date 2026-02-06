def calculadora():
    print("=== Calculadora ===")
    print("Operações: + (soma), - (subtração), * (multiplicação), / (divisão)")
    
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            operacao = input("Digite a operação (+, -, *, /): ")
            num2 = float(input("Digite o segundo número: "))
            
            if operacao == "+":
                resultado = num1 + num2
            elif operacao == "-":
                resultado = num1 - num2
            elif operacao == "*":
                resultado = num1 * num2
            elif operacao == "/":
                if num2 == 0:
                    print("Erro: Divisão por zero!")
                    continue
                resultado = num1 / num2
            else:
                print("Operação inválida!")
                continue
            
            print(f"Resultado: {num1} {operacao} {num2} = {resultado}\n")
            
            continuar = input("Deseja fazer outro cálculo? (s/n): ")
            if continuar.lower() != "s":
                break
        except ValueError:
            print("Entrada inválida! Digite números válidos.\n")

if __name__ == "__main__":
    calculadora()