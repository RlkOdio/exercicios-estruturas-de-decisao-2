import time

# O range(10, -1, -1) significa:
# Começa no 10, para antes do -1 (ou seja, no 0) e subtrai 1 a cada passo
for i in range(10, -1, -1):
    print(i)
    time.sleep(1)  # Pausa de 1 segundo para dar realismo à contagem

print("🚀 Ignição!")
