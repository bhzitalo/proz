# 9. Número positivo, negativo ou zero: Leia um número e diga se ele é positivo, negativo ou igual a zero.

# Recebe um número
num = int(input('Digite um número: '))

# se o número for maior que zero exibe que o número é positivo
if num > 0:
    print(f'O número é positivo!')
# se o número for menor que zero exibe que o número é negativo
elif num < 0:
    print(f'O número é negativo')
# se nenhum dos dois, significa que o número é zero
else:
    print('O número vale 0')