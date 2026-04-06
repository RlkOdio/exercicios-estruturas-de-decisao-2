# Solicita a velocidade do usuário
velocidade = float(input("Digite a velocidade do carro em Km/h: "))

# Define o limite permitido
limite = 80

# Verifica se a velocidade ultrapassou o limite
if velocidade > limite:
    km_acima = velocidade - limite
    valor_multa = km_acima * 50
    
    print("-" * 30)
    print(" MULTADO! Você excedeu o limite de 80Km/h.")
    print(f"Velocidade registrada: {velocidade}Km/h")
    print(f"Km acima do limite: {km_acima}Km/h")
    print(f"Valor da multa: R$ {valor_multa:.2f}")
    print("-" * 30)
else:
    print("Siga em frente! Você está dentro do limite de velocidade.")
