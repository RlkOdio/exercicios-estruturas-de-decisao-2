# Leitura dos três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Criamos uma lista para facilitar os cálculos
numeros = [num1, num2, num3]

# Processamento dos dados
maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)
media = soma / 3

# Exibição dos resultados
print("*" * 10)
print(f"maior = {maior}")
print(f"menor = {menor}")
print(f"soma = {soma}")
print(f"media = {media:.1f}")
