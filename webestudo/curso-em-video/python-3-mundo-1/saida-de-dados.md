# 🖨️ O que são Saídas de Dados?
Saída de dados é tudo o que o programa envia para o usuário como resposta ou resultado de alguma ação , geralmente usando o `print()`.

## 🖨️ `print()` — A função mais comum
```python
print("Olá, mundo!")
```
Saída: 
```
Olá, Mundo!
```

## 🔢 Saída com variáveis
```python
nome = "Italo"
idade = 24
print("Nome:", nome)
print("Idade:", idade)
```

Saída:
```
Nome: Italo
Idade: 20
```

## ✨ Formatando com f-strings
Forma mais moderna e bonita de formatar:
```python
nome = "Italo"
idade = 24
print(f"Olá, {nome}! Você tem {idade} anos.")
```

Saída:
```
Olá, Italo! Você tem 24 anos.
```

## 📜 Formatando com .format()
Outra forma de formatar, um pouco mais antiga:
```python
nome = "Italo"
idade = 24
print("Olá, {}! Você tem {} anos.".format(nome, idade))
```

Saída:
```
Olá, Italo! Você tem 24 anos.
```

## 🔄 Controlando o final e o separador
- `end=`: muda o final da linha (por padrão é \n, quebra de linha)
- `sep=`: muda o separador entre os itens
```python
print("Olá", "mundo", sep=" - ", end="!\n")
```

Saída:
```
Olá - mundo!
```