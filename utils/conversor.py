"""
Módulo de conversão de unidades de temperatura.

Este script permite ao usuário converter valores de temperatura entre as escalas 
Celsius e Fahrenheit. Ele solicita a temperatura, a escala de destino (C ou F) 
e exibe o resultado formatado.
"""

def executar():
    """Executa o conversor de temperatura interativo.

    Solicita um valor de temperatura e a unidade de destino (Celsius ou Fahrenheit). 
    Realiza o cálculo de conversão e exibe o resultado formatado com duas casas decimais.
    """
    try:
        print("\n--- Conversor de Temperatura ---")
        temp = float(input("Digite a temperatura: "))
        tipo = input("Converter para (C)elsius ou (F)ahrenheit? ").strip().upper()

        if tipo == 'C':
            resultado = (temp - 32) * 5/9
            print(f"{temp}°F = {resultado:.2f}°C")
        elif tipo == 'F':
            resultado = (temp * 9/5) + 32
            print(f"{temp}°C = {resultado:.2f}°F")
        else:
            print("Tipo inválido.")
    except ValueError:
        print("Valor inválido.")