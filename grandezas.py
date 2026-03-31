while True:
    print("\n" + "*" * 30)
    print("CÁLCULO DE GRANDEZAS ELÉTRICAS")
    print("*" * 30)
    print("1. Tensão (em Volt)")
    print("2. Resistência (em Ohm)")
    print("3. Corrente (em Ampére)")
    print("4. Sair do programa")
    print("*" * 30)
    
    opcao = input("Qual grandeza deseja calcular? ")

    if opcao == '1':
        # Cálculo da Tensão: U = R * I
        r = float(input("Informe o valor da Resistência (Ω): "))
        i = float(input("Informe o valor da Corrente (A): "))
        u = r * i
        print(f"\n>> Resultado: Tensão = {u:.2f} V")

    elif opcao == '2':
        # Cálculo da Resistência: R = U / I
        u = float(input("Informe o valor da Tensão (V): "))
        i = float(input("Informe o valor da Corrente (A): "))
        if i != 0:
            r = u / i
            print(f"\n>> Resultado: Resistência = {r:.2f} Ω")
        else:
            print("\n❌ Erro: A corrente não pode ser zero!")

    elif opcao == '3':
        # Cálculo da Corrente: I = U / R
        u = float(input("Informe o valor da Tensão (V): "))
        r = float(input("Informe o valor da Resistência (Ω): "))
        if r != 0:
            i = u / r
            print(f"\n>> Resultado: Corrente = {i:.2f} A")
        else:
            print("\n❌ Erro: A resistência não pode ser zero!")

    elif opcao == '4':
        print("Saindo do programa... Até logo!")
        break

    else:
        print("\n⚠️ Opção inválida! Por favor, escolha um número de 1 a 4.")