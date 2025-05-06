# 10. Contar vogais: Peça uma palavra e conte quantas vogais ela tem (a, e, i, o, u)

# Solicita uma palavra ao usuário
palavra = input('Digite uma palavra: ')

# Inicializa um contador de vogais
quantidade_vogais = 0

# Percorre cada letra da palavra
for letra in palavra:
    # Verifica se a letra (em minúsculo) é uma vogal
    if letra.lower() in 'aeiou':
        quantidade_vogais += 1  # Soma 1 se for vogal

# Exibe o resultado final
print(f'A palavra \'{palavra}\' tem {quantidade_vogais} vogais.')


