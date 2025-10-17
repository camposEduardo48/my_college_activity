list = []

# len() => serve para contar a quantidade de itens contidos dentro do objeto


def incrementNew():
    # x = len(list)
    print("Inicio")
    while len(list) < 10:

        receiveData = input("Insira item: ")
        receivedItem = receiveData

        if len(receivedItem) > 0:
            list.append(receivedItem)
            print(len(list))
        if len(list) == 10:
            return print(f'Temos {len(list)} itens, a condição foi satisfeita')
        else:
            print("********************** Dados inválidos! **********************")


incrementNew()
