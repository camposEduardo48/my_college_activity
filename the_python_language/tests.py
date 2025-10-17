list = []


def incrementNew():
    receiveData = input("Insira nome: ")
    receivedItem = receiveData
    list.append(receivedItem)
    return print(f"{list}")


incrementNew()
