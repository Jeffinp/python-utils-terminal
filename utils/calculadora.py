"""
Módulo de calculadora simples para operações matemáticas básicas.
"""
def executar():
    print("\n--- Calculadora Simples ---")
    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        op = input("Operação (+, -, *, /): ").strip()

        match op:
            case '+': print(f"Resultado: {a + b}")
            case '-': print(f"Resultado: {a - b}")
            case '*': print(f"Resultado: {a * b}")
            case '/': print(f"Resultado: {a / b if b != 0 else 'Divisão por zero'}")
            case _: print("Operação inválida.")
    except ValueError:
        print("Entrada inválida.")
