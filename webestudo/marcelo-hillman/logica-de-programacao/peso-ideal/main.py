#Um algoritmo que calcule seu peso imc de uma pessoa

#Recebendo os dados do usuário
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = peso/(altura**2)

#Classificando do IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso ideal"
elif imc < 30:
    classificacao = "Sobrepeso"
elif imc < 35:
    classificacao = "Obesidade grau 1"
elif imc < 40:
    classificacao = "Obesidade grau 2"
else:
    classificacao = "Obesidade grau 3"

#Exibindo os resultados
print("-----------------------------")
print("     CALCULADORA DE IMC      ")
print("        Bem-vindo(a)         ")
print("-----------------------------")
print(f"Olá, {nome} {sobrenome}!")
print(f"Você tem {altura}m de altura.")
print(f"Você pesa {peso}kg.")
print(f"Seu IMC é {imc:.4}")
print(classificacao)
print("-----------------------------")
