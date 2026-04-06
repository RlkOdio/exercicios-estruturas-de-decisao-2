# Entrada de dados do usuário
usuario_digitado = input("Digite o nome de usuário: ")
senha_digitada = input("Digite a senha: ")

# Validação dos logins
# Verificamos se o par (atila e 12345) OU o par (olivi e 54321) é válido
if (usuario_digitado == "atila" and senha_digitada == "12345") or \
   (usuario_digitado == "olivi" and senha_digitada == "54321"):
    
    print("\n✅ Seja bem vindo!")
else:
    print("\n❌ Usuário e senha não conferem")
