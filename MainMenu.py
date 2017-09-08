import Config.ConfigMenu

def escolha():
    option = input("[1]:Game \n[2]:Config \n-> ")

    if option == '1' or option == 'Game':
        print("JOGO")
    elif option == '2' or option == 'Config':
        configMenu = Config.ConfigMenu.ConfigMenu(5)
        configMenu.ShowMenu()
    else:
        print("Opção Invalida")
        escolha()


escolha()
    
