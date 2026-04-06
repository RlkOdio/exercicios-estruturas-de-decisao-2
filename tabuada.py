# Solicita o número ao usuário
print("*" * 30)
num = int(input("Informe o número da tabuada: "))
print("*" * 30)

# O laço range(1, 11) vai de 1 até 10
for i in range(1, 11):
    resultado = i * num
    print(f"{i} x {num} = {resultado}")
