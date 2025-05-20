#Programa coleta nome e sobrenome do usuario e mostra uma mensagem de saudacao ao curso de logica de programacao
#Exercicio desenvolvido na aula https://youtu.be/M2Ow2ZUX-jk?si=7ixNelyzPjxARnII

nome = input("Digite seu nome: ") #Recebe o nome do usuário
sobrenome = input("Digite seu sobrenome: ") #Recebe o sobrenome do usuário
ano_nasc = int(input("Digite seu ano de nascimento: ")) #Recebe o ano de nascimento do usuário
idade = (2025 - ano_nasc) #Calcula a idade do usuário e armazena na variável "idade"

print(f"Olá {nome} {sobrenome}, bem vindo(a) ao curso de Lógica de Programação!") #Exibe uma mensagem de boas vindas
print(f"Você nasceu em {ano_nasc} e tem {idade} anos de idade. ") #Exibe a idade do usuário