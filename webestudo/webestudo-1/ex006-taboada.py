# 6. Tabuada: Peça um número e mostre a tabuada dele de 1 a 10

# Solicita um número ao usuário
numero = int(input('Digite um número para ver a tabuada: '))

# Laço de repetição para gerar a tabuada de 1 a 10
for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')