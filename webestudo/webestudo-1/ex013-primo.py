# 13. Verificador de número primo: Peça um número e diga se ele é primo (divisível apenas por 1 e por ele mesmo). 

# Solicita um número ao usuário
numero = int(input('Digite um número: '))

# Inicializa um contador de divisores
divisores = 0

# Testa todos os números de 1 até o número digitado
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores += 1  # Conta quantos divisores o número tem

# Um número é primo se tiver exatamente 2 divisores (1 e ele mesmo)
if divisores == 2:
    print(f'O número {numero} é primo.')
else:
    print(f'O número {numero} não é primo.')