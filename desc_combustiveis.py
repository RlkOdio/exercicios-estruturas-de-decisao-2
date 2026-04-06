# Entrada de dados
litros = float(input("Digite a quantidade de litros vendidos: "))
tipo = input("Digite o tipo de combustível (A-Álcool, G-Gasolina): ").strip().upper()

# Preços base
preco_gasolina = 4.95
preco_alcool = 2.89

# Processamento
valor_total = 0
valido = True

if tipo == 'A':
    # Regras do Álcool
    if litros <= 20:
        desconto = 0.03  # 3%
    else:
        desconto = 0.05  # 5%
    valor_total = litros * (preco_alcool * (1 - desconto))

elif tipo == 'G':
    # Regras da Gasolina
    if litros <= 20:
        desconto = 0.04  # 4%
    else:
        desconto = 0.06  # 6%
    valor_total = litros * (preco_gasolina * (1 - desconto))

else:
    print("Tipo de combustível inválido!")
    valido = False

# Exibição do resultado
if valido:
    print("-" * 30)
    print(f"Combustível: {'Álcool' if tipo == 'A' else 'Gasolina'}")
    print(f"Quantidade: {litros} litros")
    print(f"Valor a pagar: R$ {valor_total:.2f}")
    print("-" * 30)
