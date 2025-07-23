"""
Módulo de calculadora que realiza operações matemáticas básicas.

Este script solicita ao usuário dois números e uma operação (+, -, *, /), 
executa o cálculo correspondente e exibe o resultado. 
O tratamento de erros está incluído para entradas não numéricas e divisão por zero.
"""
def executar():
    """
    Executa a calculadora interativa.

    Solicita dois números e uma operação, depois exibe o resultado. 
    Valida a entrada para garantir que os valores sejam numéricos e a operação seja válida.
    """
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