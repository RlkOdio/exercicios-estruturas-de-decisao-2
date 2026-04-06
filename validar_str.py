# Recebe a entrada do usuário
entrada = input("Digite algo: ")

# .strip() remove espaços em branco extras
# Se a string resultante for vazia, o Python a interpreta como False
if not entrada.strip():
    print("Dado inválido")
else:
    print(f"Você digitou: {entrada}")
