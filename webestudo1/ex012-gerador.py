# 12. Gerador de sequência: Peça um número e gere uma sequência de 0 até esse número, pulando de 2 em 2

# Solicita um número ao usuário
contador = int(input('Digite um número: '))

# Gera e exibe a sequência de 0 até o número informado, pulando de 2 em 2
for i in range(0, contador + 1, 2):
    print(i)