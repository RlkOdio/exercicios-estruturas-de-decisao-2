# Solicita a distância da viagem
distancia = float(input("Digite a distância que deseja percorrer (em Km): "))

# Estrutura condicional para definir o valor da tarifa
if distancia <= 200:
    preco_por_km = 0.50
else:
    preco_por_km = 0.45

# Cálculo do preço total
preco_total = distancia * preco_por_km

# Exibição do resultado
print("-" * 35)
print(f"Distância da viagem: {distancia} Km")
print(f"Preço por Km aplicado: R$ {preco_por_km:.2f}")
print(f"Valor total da passagem: R$ {preco_total:.2f}")
print("-" * 35)
