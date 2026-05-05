nome_empresa = input("Digite o nome da empresa: ")
saldo_inicial = int(input("Digite o saldo inicial: "))
caminhao = 0
opcao = 0

while opcao != 5:
    print("1 - Comprar caminhão (+1200 no saldo)")
    print("2 - Realizar entrega (-30000 do saldo, +1 caminhão)")
    print("3 - Mostrar frota atual")
    print("4 - Manutenção (-30000 do saldo)")
    print("5 - Sair")
    
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        saldo_inicial += 1200
        print("Entrega realizada")

    elif opcao == 2:
        if saldo_inicial >= 30000:
            saldo_inicial -= 30000
            caminhao += 1
            print("Entrega realizada")
        else:
            print("Sem saldo")

    elif opcao == 3:
        print("Frota atual:", caminhao)

    elif opcao == 4:
        if saldo_inicial >= 30000:
            saldo_inicial -= 30000
            print("Manutenção realizada")
        else:
            print("Saldo insuficiente")

    elif opcao == 5:
        print("Saldo final: R$", saldo_inicial)
        print("Frota:", caminhao)
        print("Encerrando programa...")

    else:
        print("Opção inválida, tente novamente")
