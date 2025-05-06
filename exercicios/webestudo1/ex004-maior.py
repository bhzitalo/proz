# 4. Leia dois números e informe qual é o maior, ou se são iguais

# Solicita o primeiro número
numero1 = float(input('Digite o primeiro número: '))

# Solicita o segundo número
numero2 = float(input('Digite o segundo número: '))

# Verifica se o primeiro número é maior que o segundo
if numero1 > numero2:
    print(f'O primeiro número ({numero1}) é maior que o segundo ({numero2}).')
# Verifica se o segundo número é maior que o primeiro
elif numero2 > numero1:
    print(f'O segundo número ({numero2}) é maior que o primeiro ({numero1}).')
# Se os números forem iguais
else:
    print(f'Os dois números ({numero1} e {numero2}) são iguais.')