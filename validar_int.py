# Recebe a entrada como string primeiro para evitar erro de conversão
entrada = input("Digite um número inteiro: ").strip()

# Verifica se a entrada está vazia
if entrada == "":
    print("Dado inválido")
else:
    # Tenta converter para inteiro apenas se não estiver em branco
    try:
        numero = int(entrada)
        print(f"O número digitado foi: {numero}")
    except ValueError:
        # Caso o usuário digite letras ou símbolos em vez de números
        print("Dado inválido! Por favor, digite apenas números inteiros.")
