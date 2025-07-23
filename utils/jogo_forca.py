"""
Módulo do jogo da forca para terminal.
""" 
import random

def executar():
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

        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_descobertas[i] = letra
        else:
            if letra not in letras_erradas:
                tentativas -= 1
                letras_erradas.append(letra)

    if '_' not in letras_descobertas:
        print(f"\nParabéns! Você acertou: {palavra}")
    else:
        print(f"\nVocê perdeu! A palavra era: {palavra}")
