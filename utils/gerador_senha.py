"""
Módulo para geração de senhas seguras.

Este script cria uma senha aleatória com base no comprimento definido pelo usuário. 
A senha pode incluir uma combinação de letras maiúsculas, minúsculas, 
números e caracteres especiais para garantir maior segurança.
"""

import random
import string

def executar():
    """
    Executa o gerador de senhas interativo.

    Solicita ao usuário o comprimento desejado para a senha e, em seguida, 
    gera uma senha aleatória usando uma combinação de caracteres ASCII, 
    dígitos e pontuação.
    """
    print("\n--- Gerador de Senha ---")
    try:
        tamanho = int(input("Digite o tamanho da senha: "))
        if tamanho <= 0:
            print("O tamanho deve ser um número positivo.")
            return
        
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        print(f"Senha gerada: {senha}")
    except ValueError:
        print("Digite um número válido.")