# 8. Verificador de senha: Peça uma senha e só permita continuar se for igual a "coxinha", usando while.

# Pede a senha ao usuário
senha = input('Digite a senha: ')

# Enquanto a senha estiver incorreta, repete o pedido
while senha != 'coxinha':
    print('Senha incorreta. Tente novamente.')
    senha = input('Digite a senha: ')

# Quando a senha for correta, o loop acaba e continua o programa
print('Senha correta. Acesso liberado!')