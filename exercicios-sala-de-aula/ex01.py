# Exercício 1: Preço a pagar
# Crie um programa que pergunte ao usuário o valor do café (um número) e pergunte para ele quantos cafés ele irá querer comprar e apresente o resultado a pagar.

print("="*30) #Exibe uma mensagem inicial
print("          CAFÉ BONJOUR")
print("    O melhor café da região")
print("="*30)

print("Escolha seu café:") #exibe as opções disponíveis
print("[1]Café preto...........R$ 2,50")
print("[2]Café com leite.......R$ 3,50")
print("[3]Café expresso........R$ 5,00")
print("[4]Cappuccino...........R$ 7,50")
print("---")

preco_cafe = 0 #define um preço inicial para o café = 0

escolha = float(input("Escolha uma opção: ")) #recebe a escolha do user

#estrutura que define o preço do café com base na escolha do user
if escolha == 1: 
    preco_cafe = 2.50
elif escolha == 2:
    preco_cafe = 3.50
elif escolha == 3:
    preco_cafe = 5.00
elif escolha == 4:
    preco_cafe = 7.50
else:
    preco_cafe = 0

quantidade = float(input("Quantidade: ")) #recebe e exibe a quantidade
total = (preco_cafe * quantidade) #faz o calculo (escolha x quantidade)

print("="*30)
print(f"Total a pagar: R$ {total}") #exibe o total a pagar

print("="*30) #Exibe uma mensagem final
print("           OBRIGADO")
print("         Volte Sempre! ")
print("="*30)