# 🧩 Tipos Primitivos
Tipos primitivos (ou tipos básicos) são os tipos de dados mais simples que existem em uma linguagem de programação. Eles representam valores únicos e diretos, como números, textos ou valores lógicos.

Em Python, os principais tipos primitivos são:

### 🔢 _int_ — Números inteiros
São números sem parte decimal. </br>
```python
idade = 20
```

### 🔣 _float_ — Números reais (com ponto flutuante)
São números com parte decimal. </br>
```python
altura = 1.75
```

### 📝 _str_ — Cadeia de caracteres (texto / string)
Tudo o que estiver entre aspas (simples ou duplas).

### ✅ _bool_ — Valores booleanos (lógico)
Usado para representar **Verdadeiro** ou **Falso**.
```python
estudando = True
cansado = False
```

## 🧪 Descobrindo o tipo de uma variável

Use a função `type()` para descobrir o tipo de um dado:

```python
print(type(idade))     # <class 'int'>
print(type(altura))    # <class 'float'>
print(type(ligado))    # <class 'bool'>
print(type(nome))      # <class 'str'>
```



