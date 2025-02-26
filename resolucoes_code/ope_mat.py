# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

def operacoes_matematicas():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Escolha a operação (+, -, *, /): ")
    
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro: divisão por zero não é permitida."
    else:
        resultado = "Operação inválida."
    
    print("Resultado:", resultado)

if __name__ == "__main__":
    operacoes_matematicas()
