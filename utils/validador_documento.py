
"""
Módulo para validação de documentos brasileiros (CPF e CNPJ).

Este script oferece funções para verificar a validade de números de CPF e CNPJ 
com base nos algoritmos de cálculo dos dígitos verificadores. 
Ele também fornece uma interface de linha de comando para validação rápida.
"""

import re

def validar_cpf(cpf: str) -> bool:
    """
    Valida um número de CPF.

    Args:
        cpf: O número de CPF a ser validado, podendo conter máscaras.

    Returns:
        True se o CPF for válido, False caso contrário.
    """
    cpf = re.sub(r'\D', '', cpf)
    
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    
    try:
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        dig1 = (soma * 10 % 11) % 10
        
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        dig2 = (soma * 10 % 11) % 10
        
        return dig1 == int(cpf[9]) and dig2 == int(cpf[10])
    except (ValueError, IndexError):
        return False

def validar_cnpj(cnpj: str) -> bool:
    """
    Valida um número de CNPJ.

    Args:
        cnpj: O número de CNPJ a ser validado, podendo conter máscaras.

    Returns:
        True se o CNPJ for válido, False caso contrário.
    """
    cnpj = re.sub(r'\D', '', cnpj)
    
    if len(cnpj) != 14:
        return False
        
    try:
        pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        pesos2 = [6] + pesos1
        
        soma1 = sum(int(cnpj[i]) * pesos1[i] for i in range(12))
        dig1 = (11 - soma1 % 11)
        dig1 = dig1 if dig1 < 10 else 0

        soma2 = sum(int(cnpj[i]) * pesos2[i] for i in range(13))
        dig2 = (11 - soma2 % 11)
        dig2 = dig2 if dig2 < 10 else 0
        
        return dig1 == int(cnpj[12]) and dig2 == int(cnpj[13])
    except (ValueError, IndexError):
        return False

def executar():
    """
    Executa o validador de CPF/CNPJ interativo.

    Solicita ao usuário um número de documento, identifica se é CPF ou CNPJ 
    pelo comprimento e exibe o resultado da validação.
    """
    print("\n--- Validador de CPF/CNPJ ---")
    doc = input("Digite o CPF ou CNPJ: ").strip()

    doc_limpo = re.sub(r'\D', '', doc)

    if len(doc_limpo) == 11:
        print("CPF válido!" if validar_cpf(doc) else "CPF inválido.")
    elif len(doc_limpo) == 14:
        print("CNPJ válido!" if validar_cnpj(doc) else "CNPJ inválido.")
    else:
        print("Documento inválido.")
