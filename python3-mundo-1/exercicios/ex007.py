# 7. Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print('CALCULANDO A MÉDIA')
aluno = input('Digite seu nome: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

print(f'{aluno}, sua média é {media:.2f}')