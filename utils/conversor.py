
# utils/conversor.py
def executar():
    """
    Módulo de conversão de unidades e moedas.
    Esta função permite ao usuário converter temperaturas entre Celsius e Fahrenheit.
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
