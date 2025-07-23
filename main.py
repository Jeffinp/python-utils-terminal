from utils import conversor, calculadora, gerador_senha, jogo_forca, validador_documento

def menu():
    print("Bem-vindo ao menu de utilitários!")
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
    else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()