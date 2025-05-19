# 9. Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

print('CONVERSOR DE MEDIDAS')

metros = float(input('Digite um valor em metros: '))

centimetros = metros * 100
milimetros = metros * 1000

print(f'{metros} metros é igual a {centimetros:.0f} centímetros e {milimetros:.0f} milímetros.')
