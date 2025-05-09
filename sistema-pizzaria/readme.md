# Sistema para Pizzaria "Turma do Fundão"
Este código implementa um sistema simples de pedidos para uma pizzaria.
O sistema é executado no terminal e permite ao cliente selecionar o tamanho da pizza, o sabor, a bebida e exibe o valor total do pedido.

Desenvolvido por Cíntia, Kauan, Ítalo e Juliana. 
 O sistema é executado no terminal e permite ao cliente selecionar o tamanho da pizza, o sabor, a bebida e exibe o valor total do pedido.

### ✅ Funcionalidades:
Boas-vindas: Exibe uma mensagem de apresentação da pizzaria.
Escolha do tamanho da pizza:
    [1] Pequena - R$ 19,90

    [2] Média - R$ 25,90

    [3] Grande - R$ 35,90
O sistema armazena o tamanho escolhido e define o preço correspondente.
Quantidade de pizzas: O cliente informa quantas pizzas deseja (apesar de o sistema não multiplicar o valor pela quantidade — isso poderia ser uma melhoria futura).

Escolha do sabor da pizza:

[1] Calabresa

[2] Frango

[3] À Moda

Escolha da bebida:

[1] Coca-Cola - R$ 8,50

[2] Guaraná - R$ 7,50

[3] Suco Maracujá - R$ 8,00
O sistema armazena o sabor escolhido e define o preço correspondente.

Cálculo do total: Soma o valor da pizza (apenas uma unidade) e da bebida escolhida.

Confirmação do pedido: Exibe as informações do pedido, incluindo sabor da pizza, tamanho, bebida e valor total.

📌 Observações Técnicas:
O código usa input() para capturar as escolhas do usuário e print() para exibir mensagens.

A lógica de seleção é feita com estruturas condicionais (if/elif/else).

Uma variável total calcula o valor final do pedido.

Apesar de solicitar a quantidade de pizzas, o total não é multiplicado pela quantidade informada, o que poderia ser corrigido para maior precisão.