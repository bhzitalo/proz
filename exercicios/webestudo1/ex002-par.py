# 2. Par ou ímpar: Leia um número inteiro e diga se ele é par ou ímpar

# Solicita um número inteiro ao usuário
numero = int(input('Digite um número inteiro: '))

# Verifica se o número é divisível por 2
if numero % 2 == 0:
    print(f'O número {numero} é PAR.')  # Se o resto da divisão por 2 for 0, é par
else:
    print(f'O número {numero} é ÍMPAR.')  # Caso contrário, é ímpar
