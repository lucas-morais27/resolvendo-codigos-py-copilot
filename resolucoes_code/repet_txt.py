# Vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

def repetir_textos():
    texto = input("Digite um texto: ")
    vezes = int(input("Digite um número inteiro: "))
    resultado = texto * vezes
    print("Resultado:", resultado)

if __name__ == "__main__":
    repetir_textos()
