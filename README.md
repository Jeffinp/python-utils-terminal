# Python Utils Terminal

![GitHub](https://img.shields.io/github/license/jeffinp/python-utils-terminal) ![Python](https://img.shields.io/badge/python-3.10%2B-blue)

Este é um projeto de utilitários de linha de comando em Python, oferecendo uma coleção de ferramentas interativas para diversas finalidades. O objetivo é fornecer uma suíte de scripts simples e eficientes para tarefas do dia a dia, com código claro e bem documentado.

## Funcionalidades

O projeto inclui os seguintes módulos:

- **Calculadora Simples**: Realiza operações matemáticas básicas (+, -, *, /).
- **Conversor de Temperatura**: Converte temperaturas entre Celsius e Fahrenheit.
- **Gerador de Senha**: Cria senhas seguras com base no tamanho especificado pelo usuário.
- **Jogo da Forca**: Uma implementação do clássico jogo de adivinhação de palavras.
- **Validador de Documentos**: Verifica a validade de números de CPF e CNPJ com base nos algoritmos oficiais.

## Como Usar

### Pré-requisitos

- Python 3.10 ou superior

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/jeffinp/python-utils-terminal.git
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

    Após a execução, um menu interativo será exibido, permitindo que você escolha qual utilitário deseja usar.

## Estrutura do Projeto

```
/python-utils-terminal
├── utils/
│   ├── __init__.py
│   ├── calculadora.py
│   ├── conversor.py
│   ├── gerador_senha.py
│   ├── jogo_forca.py
│   └── validador_documento.py
├── .gitignore
├── main.py
├── requirements.txt
├── LICENSE
└── README.md
```

- **`main.py`**: Ponto de entrada da aplicação. Exibe o menu e gerencia a navegação entre os utilitários.
- **`utils/`**: Pacote contendo os módulos com a lógica de cada funcionalidade.
- **`LICENSE`**: Arquivo de licença do projeto (MIT).

## Contribuição

Contribuições são muito bem-vindas! Se você tiver ideias para novas funcionalidades, melhorias ou correções de bugs, sinta-se à vontade para:

1.  Fazer um *fork* do projeto.
2.  Criar uma nova *branch* (`git checkout -b feature/nova-feature`).
3.  Fazer *commit* de suas alterações (`git commit -m 'Adiciona nova feature'`).
4.  Fazer *push* para a *branch* (`git push origin feature/nova-feature`).
5.  Abrir um *Pull Request*.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
