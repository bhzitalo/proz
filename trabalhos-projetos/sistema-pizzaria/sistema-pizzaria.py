# Este código implementa um sistema simples de pedidos para uma pizzaria.

# Apresentação ao usuário
print("---------------------------------")
print("         TURMA DO FUNDÃO         ")
print("     A melhor pizza do bairro    ")

# Primeira parte – Escolha do tamanho
print("---------------------------------")
print("ESCOLHA O TAMANHO DA SUA PIZZA")
print("[1] BROTINHO:         R$ 17,90")  # Individual
print("[2] PEQUENA:          R$ 27,90")  # Serve 1-2 pessoas
print("[3] MÉDIA:            R$ 39,90")  # Serve 2-3 pessoas
print("[4] GRANDE:           R$ 49,90")  # Serve 3-4 pessoas
print("[5] GIGANTE:          R$ 59,90")  # Serve 4-5 pessoas ou mais
print("---")

tamanho_pizza = int(input("DIGITE UMA OPÇÃO: "))  # Recebe a escolha do usuário: 1, 2 , 3, 4 ou 5
valor_pizza = 0  # Inicia em 0 e recebe o valor da pizza

# Estrutura para receber a resposta do usuário
if tamanho_pizza == 1: # Broto
    tamanho_pizza = "BROTO"
    valor_pizza = 17.90
elif tamanho_pizza == 2: # Pequena
    tamanho_pizza = "P"
    valor_pizza = 27.90
elif tamanho_pizza == 3: # Média
    tamanho_pizza = "M"
    valor_pizza = 39.90
elif tamanho_pizza == 4: # Grande
    tamanho_pizza = "G"
    valor_pizza = 49.90
elif tamanho_pizza == 5: # Gigante
    tamanho_pizza = "GG"
    valor_pizza = 59.90
else:
    print("Opção inválida! Pedido Cancelado") # Se o usuário digitar qualquer outro valor, o pedido será cancelado no final.

# Segunda parte – Escolha do sabor da pizza
print("---------------------------------")
print("ESCOLHA O SABOR DA SUA PIZZA")
print("[1] CALABRESA                    ")
print("[2] FRANGO C/ CATUPIRY           ")
print("[3] PORTUGUESA                   ")  
print("[4] QUATRO QUEIJOS               ")  
print("[5] A MODA                       ")  
print("---")

sabor_pizza = int(input("DIGITE UMA OPÇÃO? "))  # Variável para guardar o sabor da pizza

if sabor_pizza == 1: # Estrutura para definir o sabor da pizza
    sabor_pizza = "CALABRESA"
elif sabor_pizza == 2:
    sabor_pizza = "FRANGO C/ CATUPIRY"
elif sabor_pizza == 3:
    sabor_pizza = "PORTUGUESA"
elif sabor_pizza == 4:
    sabor_pizza = "QUATRO QUEIJOS"
elif sabor_pizza == 5:
    sabor_pizza = "A MODA"
else:
    print("Opção inválida! Pedido Cancelado")
    sabor_pizza = "CANCELADO"

# Terceira parte – Escolha da bebida
print("---------------------------------")
print("ESCOLHA O QUE VAI BEBER")
print("[0] PULAR")
print("[1] COCA-COLA LATA   R$ 6,50")
print("[2] COCA-ZERO LATA   R$ 6,50")
print("[3] GUARANÁ LATA     R$ 7,50")
print("[4] SUCO DEL VALLE   R$ 4,00")
print("[5] H2OH! LIMÃO      R$ 6,80")
print("---")

sabor_bebida = int(input("DIGITE UMA OPÇÃO? "))
valor_bebida = 0  # Inicializa o valor

if sabor_bebida == 0:
    sabor_bebida = ""
    valor_bebida = 0
elif sabor_bebida == 1:
    sabor_bebida = "COCA-COLA LATA"
    valor_bebida = 6.50
elif sabor_bebida == 2:
    sabor_bebida = "COCA-ZERO LATA"
    valor_bebida = 6.50
elif sabor_bebida == 3:
    sabor_bebida = "GUARANÁ LATA"
    valor_bebida = 7.50
elif sabor_bebida == 4:
    sabor_bebida = "SUCO DEL VALLE"
    valor_bebida = 4.00
elif sabor_bebida == 5:
    sabor_bebida = "H2OH! LIMÃO"
    valor_bebida = 6.80
else:
    print("Opção inválida! Pedido Cancelado")

# Quarta parte – Confirmação do pedido
print("---------------------------------")
print("PEDIDO FINALIZADO")
print("")
print(f"PIZZA: {sabor_pizza} [{tamanho_pizza}] R$ {valor_pizza:.2f}")
print(f"BEBIDA: {sabor_bebida} R$ {valor_bebida:.2f}")
print(f"TOTAL: R$ {valor_bebida + valor_pizza:.2f}")
