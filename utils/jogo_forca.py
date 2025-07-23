"""
Módulo que implementa o clássico jogo da forca para o terminal.

O jogador deve adivinhar uma palavra secreta, letra por letra, 
antes que o número de tentativas se esgote. O jogo seleciona a palavra 
de uma lista predefinida e exibe o progresso a cada rodada.
"""

import random

def executar():
    """
    Executa o jogo da forca interativo.

    Uma palavra é escolhida aleatoriamente de uma lista. O jogador insere letras 
    para adivinhar a palavra, com um limite de 6 tentativas para erros. 
    O estado do jogo é exibido a cada rodada.
    """
    print("\n--- Jogo da Forca ---")
    palavras = ['python', 'terminal', 'desenvolvedor', 'projeto', 'github']
    palavra = random.choice(palavras).lower()
    letras_descobertas = ['_' for _ in palavra]
    tentativas = 6
    letras_erradas = []

    while tentativas > 0 and '_' in letras_descobertas:
        print("\nPalavra:", ' '.join(letras_descobertas))
        print(f"Tentativas restantes: {tentativas}")
        print("Letras erradas:", ', '.join(letras_erradas))

        letra = input("Digite uma letra: ").lower()
        if len(letra) != 1 or not letra.isalpha():
            print("Digite apenas uma letra.")
            continue

        if letra in letras_descobertas or letra in letras_erradas:
            print("Você já tentou esta letra.")
            continue

        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_descobertas[i] = letra
        else:
            tentativas -= 1
            letras_erradas.append(letra)

    if '_' not in letras_descobertas:
        print(f"\nParabéns! Você acertou a palavra: {palavra}")
    else:
        print(f"\nVocê perdeu! A palavra era: {palavra}")