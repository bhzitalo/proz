# Solicita ao usuário um número decimal
numero = int(input("Digite um número decimal: "))

# Cria uma variável para guardar o resultado final em binário
binario = ""

# Se o número digitado for 0, o binário também é 0
if numero == 0:
    binario = "0"
else:
    # Enquanto o número for maior que 0, dividinda por 2
    while numero > 0:
        resto = numero % 2              # Pega o resto da divisão por 2 (0 ou 1)
        binario = str(resto) + binario  # Adiciona o dígito binário à esquerda do resultado
        numero = numero // 2            # Atualiza o número com a parte inteira da divisão por 2

# Mostra o número convertido em binário
print("Número em binário:", binario)