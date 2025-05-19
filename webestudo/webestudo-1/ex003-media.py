# 3. Média de três notas: Leia três notas de um aluno, calcule a média e informe se ele foi aprovado (média ≥ 7).

# Solicita as notas ao usuário
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

# Calcula a média das três notas
media = (nota1 + nota2 + nota3) / 3

# Exibe a média
print(f'A média é igual a: {media}')

# Verifica se a média é maior ou igual a 7 para aprovar o aluno
if media >= 7:
    print('APROVADO')  # Se a média for maior ou igual a 7, o aluno é aprovado
else:
    print('REPROVADO')  # Caso contrário, o aluno é reprovado
