# Criamos uma lista vazia para armazenar os números
numeros = []

# Usamos um laço para repetir a leitura 5 vezes
for i in range(1, 6):
    num = float(input(f"Digite o {i}º número: "))
    numeros.append(num)

# Exibimos os números na tela
print("-" * 20)
print("Números digitados:")
for n in numeros:
    print(n)
