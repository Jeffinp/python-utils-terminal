# Python Utils Terminal

Este é um projeto de utilitários de linha de comando em Python, oferecendo uma coleção de ferramentas interativas para diversas finalidades.

## Funcionalidades

O projeto inclui os seguintes módulos:

- **Calculadora Simples**: Realiza operações matemáticas básicas (+, -, *, /).
- **Conversor de Temperatura**: Converte temperaturas entre Celsius e Fahrenheit.
- **Gerador de Senha**: Cria senhas seguras com base no tamanho especificado.
- **Jogo da Forca**: Um jogo clássico de adivinhação de palavras.
- **Validador de Documentos**: Verifica a validade de números de CPF e CNPJ.

## Como Usar

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/python-utils-terminal.git
    cd python-utils-terminal
    ```

2.  **Instale as dependências (se houver):**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Execute o programa principal:**
    ```bash
    python main.py
    ```

    O programa apresentará um menu onde você pode escolher qual utilitário deseja usar.

## Estrutura do Projeto

```
/
├── utils/
│   ├── calculadora.py
│   ├── conversor.py
│   ├── gerador_senha.py
│   ├── jogo_forca.py
│   └── validador_documento.py
├── main.py
├── requirements.txt
└── README.md
```

- **`main.py`**: Ponto de entrada do programa, exibe o menu e chama os módulos.
- **`utils/`**: Contém os módulos com a lógica de cada funcionalidade.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.