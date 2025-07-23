
"""
Módulo principal que funciona como um hub de utilitários em linha de comando.

Este script apresenta um menu interativo que permite ao usuário selecionar e 
executar diferentes ferramentas, como calculadora, conversor de unidades, 
gerador de senhas, jogo da forca e validador de documentos. 
Cada utilitário é importado de seu respectivo módulo no pacote 'utils'.
"""

from utils import conversor, calculadora, gerador_senha, jogo_forca, validador_documento

def menu():
    """
    Exibe o menu principal e gerencia a seleção do usuário.

    O menu lista todos os utilitários disponíveis e aguarda a entrada do usuário 
    para executar a ferramenta correspondente. O loop continua até que o usuário 
    escolha a opção de sair.
    """
    while True:
        print("\nBem-vindo ao menu de utilitários!")
        print("1. Conversor de Unidades")
        print("2. Calculadora")
        print("3. Gerador de Senha")
        print("4. Jogo da Forca")
        print("5. Validador de Documento")
        print("0. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            conversor.executar()
        elif escolha == '2':
            calculadora.executar()
        elif escolha == '3':
            gerador_senha.executar()
        elif escolha == '4':
            jogo_forca.executar()
        elif escolha == '5':
            validador_documento.executar()
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
