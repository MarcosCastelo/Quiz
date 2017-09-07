def escolha():
    option = input("[1]:Game \n[2]:Config \n-> ")

    if option == '1' or option == 'Game':
        print("Vc entrou no game")
    elif option == '2' or option == 'Config':
        print("Vc entrou nas configurações")
    else:
        print("Opção Invalida")
        escolha()


escolha()
    
