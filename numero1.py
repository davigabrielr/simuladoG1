valor_carga = int(input("Digite o valor da carga: "))
codigo = int(input("Qual seu código (1-Berlin, 2-Lisboa, 3-Paris): "))

if codigo == 1:
    valor_final = valor_carga * 1.05
    print("Destino: Berlin")
    print("Valor da carga: R$", valor_carga)
    print("Total = R$", valor_final)

elif codigo == 2:
    valor_final = valor_carga * 1.07
    print("Destino: Lisboa")
    print("Valor da carga: R$", valor_carga)
    print("Total = R$", valor_final)

elif codigo == 3:
    valor_final = valor_carga * 1.10
    if valor_final >= 1000:
        print("Destino: Paris")
        print("Valor da carga: R$", valor_carga)
        print("Total = R$", valor_final)
    else:
        print("Valor final menor que 1000, não permitido.")

else:
    print("Código inválido")
