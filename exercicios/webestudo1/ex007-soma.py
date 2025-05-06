# 7. Soma de 1 até N: Peça um número X e calcule a soma de todos os números de 1 até x

# Solicita um número ao usuário
x = int(input('Digite um número: '))

# Inicializa a variável que guardará a soma
soma = 0

# Faz a soma de 1 até X
for i in range(1, x + 1):
    soma += i  # soma = soma + i

# Exibe o resultado
print(f'A soma de 1 até {x} é {soma}')