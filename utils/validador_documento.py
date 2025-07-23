import re  # Importa o módulo de expressões regulares

def validar_cpf(cpf):
    """
    Valida um CPF (Cadastro de Pessoa Física).
    Remove caracteres não numéricos, verifica tamanho e repetições,
    calcula os dígitos verificadores e compara com os informados.
    """
    cpf = re.sub(r'\D', '', cpf)
    
    # Verifica se o CPF tem 11 dígitos e não é uma sequência repetida
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    dig1 = (soma * 10 % 11) % 10
    # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    dig2 = (soma * 10 % 11) % 10
    # Retorna True se os dígitos verificadores estiverem corretos
    return dig1 == int(cpf[9]) and dig2 == int(cpf[10])

def validar_cnpj(cnpj):
    """
    Valida um CNPJ (Cadastro Nacional da Pessoa Jurídica).
    Remove caracteres não numéricos, verifica tamanho,
    calcula os dígitos verificadores e compara com os informados.
    """
    cnpj = re.sub(r'\D', '', cnpj)
    # Verifica se o CNPJ tem 14 dígitos
    if len(cnpj) != 14:
        return False
    # Pesos para cálculo dos dígitos verificadores
    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos2 = [6] + pesos1
    # Calcula o primeiro dígito verificador
    soma1 = sum(int(cnpj[i]) * pesos1[i] for i in range(12))
    dig1 = 11 - soma1 % 11
    dig1 = dig1 if dig1 < 10 else 0
    # Calcula o segundo dígito verificador
    soma2 = sum(int(cnpj[i]) * pesos2[i] for i in range(13))
    dig2 = 11 - soma2 % 11
    dig2 = dig2 if dig2 < 10 else 0
    # Retorna True se os dígitos verificadores estiverem corretos
    return dig1 == int(cnpj[12]) and dig2 == int(cnpj[13])

def executar():
    """
    Executa o validador de CPF/CNPJ via terminal.
    Solicita ao usuário o documento, identifica o tipo e exibe o resultado.
    """
    print("\n--- Validador de CPF/CNPJ ---")
    doc = input("Digite o CPF ou CNPJ: ").strip()

    # Identifica se é CPF ou CNPJ pelo tamanho
    if len(re.sub(r'\D', '', doc)) == 11:
        print("CPF válido!" if validar_cpf(doc) else "CPF inválido.")
    elif len(re.sub(r'\D', '', doc)) == 14:
        print("CNPJ válido!" if validar_cnpj(doc) else "CNPJ inválido.")
    else:
        print("Documento inválido.")
