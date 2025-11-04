list = []

# len() => serve para contar a quantidade de itens contidos dentro do objeto


# Função para adicionar itens dentro do array fazendo o loop com o while até a condigção ser satisfeita
def incrementNew():
    print("Inicio")

    while len(list) < 10:
        receiveData = input("Insira item: ")
        # Fazer verificação para ver se já existe o item adicionado no array para nao duplicar
        receivedItem = receiveData

        if len(receivedItem) > 0:
            list.append(receivedItem)
            print(f"Item - {len(list)}")
        if len(list) == 10:
            print("Finalizou!")
            print(list)
            return print(f"Temos {len(list)} itens, a condição foi satisfeita")
        else:
            print("********************** Dados inválidos! **********************")
    return print(f"Temos {len(list)} itens, a condição foi satisfeita")


incrementNew()
