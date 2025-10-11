# Lembrar de sempre verificar á identação do código para não ter problemas com escopo


def testMyCode():
    # -------------- level_01 --------------
    # x = int(input("Digite um número: "))
    # num = x
    # res = True
    # if num > 0:
    #     print("O número é maior que zero")
    #     # res = True
    # elif num == 0:
    #     print("O número é igual á zero")
    #     # res = True
    # else:
    #     print("O número informado é menor que zero ou inválido")

    # -------------- level_02 --------------
    # x = int(input("Digite um número: "))
    # first = x
    # print(f"Você digitou {first}")

    # y = int(input("Digite o segundo número: "))
    # second = y
    # print(f"Você digitou {second}")

    # z = int(input("Digite o terceiro número: "))
    # third = z
    # print(f"Você digitou {third}")

    # if first > second and first > third:
    #     return print(f"{first} é o maior dos números inseridos!")

    # if second > first and second > third:
    #     return print(f"{second} é o maior dos números inseridos!")

    # if third > first and third > second:
    #     return print(f"{third} é o maior dos números inseridos!")

    # -------------- level_03 --------------
    # x = int(
    #     input(
    #         "Digite sua idade para verificar se está apto para tirar habilitação ou não: "
    #     )
    # )
    # age = x

    # if age >= 18:
    #     return print(
    #         f"Você tem {age} anos, então você está apto á tirar sua habilitação!"
    #     )
    # else:
    #     return print(f"Infelizmente você não está apto ainda para tirar habilitação")

    # -------------- level_03 --------------
    x = input("Digite seu usuário: ")
    user_name = x

    y = input("Digite sua senha:")
    password = y

    if user_name == "administrador" and password == "12345":
        return print("Login realizado com sucesso, seja bem-vindo novamente!")
    else:
        return print("Usuário ou senha inválida")


testMyCode()
