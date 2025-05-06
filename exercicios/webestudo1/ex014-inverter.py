# 14. Inverter palavra: Peça uma palavra e exiba-a invertida (ex: “python” → “nohtyp”).

# Solicita uma palavra ao usuário
palavra = input('Digite uma palavra: ')

# Inverte a palavra usando fatiamento com passo -1
palavra_invertida = palavra[::-1]

# Exibe a palavra invertida
print(f'A palavra invertida é: {palavra_invertida}')