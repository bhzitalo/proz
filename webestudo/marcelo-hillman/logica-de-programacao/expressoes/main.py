#O programa irá receber 4 notas de um aluno e vai comparar com a média da escola(6)

print("-------------------------")
print("  ESCOLA JAVALI CANSADO"  )
print("-------------------------")

contador = 1 
media = 0

while contador <= 4:
    nota = float(input(f"Digite a {contador}ª nota: "))
    media =  media + nota # (+=)
    contador = contador + 1 # (+=)
    
media_final = media / 4
print(f"A sua média é: {media_final:.2f}")

