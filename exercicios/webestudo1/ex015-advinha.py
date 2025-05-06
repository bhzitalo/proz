# 15. Jogo de adivinhação simples: O programa escolhe um número entre 1 e 10 e o usuário tenta adivinhar. Use random para gerar o número.

import random  # Importa o módulo para gerar números aleatórios

# Gera um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

# Solicita um palpite do usuário
palpite = int(input('Tente adivinhar o número entre 1 e 10: '))

# Verifica se o palpite está correto
if palpite == numero_secreto:
    print('Parabéns! Você acertou!')
else:
    print(f'Você errou! O número era {numero_secreto}.')