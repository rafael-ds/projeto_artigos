to_do_list = []

def banner(tilulo, traco, centralizar):
    # Função estetica
    # titulo --> titulo ref a opção
    # linha --> quantidade de traços do banner
    # centralizar --> centraliza o titulo no meio do banner(colocar o mesmo
    # valor usado no traço)

    l = '-' * traco
    t = tilulo

    print(l)
    print(t.center(centralizar))
    print(l)


banner('Minha To Do List', 100, 100)

def add_item():
    # *Função que adiciona um novo item ao final da lista*
    # capitalize() --- Deixa a primeira letra em maiúscula

    item = input('Novo item: ').capitalize()
    to_do_list.append(item)


def edit_item():
    # *Função que edita um elemento da lista*

    itens()

    # Variavel que guarda um valor numerico para ser usado como posição do elemento na lsita
    item = int(input('Insira o index do item:'))

    # Nome do novo item que substituira o item a ser alterado
    edt_item = input('Editar item: ')

    # Alterando o item pelo novo
    # Variavel 'item' sera a posição do item na lista
    to_do_list[item] = edt_item

    menu()

def remove_item():
    # *Função que remove o item da lista *
    itens()

     # Variavel que guarda um valor numerico para ser usado como posição do elemento na lista
    item = int(input('Insira o index do item:'))


    opc = input('Excluir item: [s] -- [n]')

    # Condição para opção de excluir ou não o item da lista
    if opc == 's':
        to_do_list.pop(item) # --> remove da lista o item informado na variavel 'item'
        print('Item removido com sucesso.')

        menu()

    elif opc == 'n':
        menu()

def itens():
    # * Função que mostra a lista enumerada
    for index, item in enumerate(to_do_list):
            print(f'{index} - {item}')


def display_item():
    # Função que mostra os itens da lista e caso estreja vazia
    # Informa que não existe elemento na lista

    if len(to_do_list) == 0:
        print('Sua lista ainda não possui itens.\n')
        menu()

    else:
        itens()
        menu()    


def clear_to_do_list():
    # Função que apaga todos os itens da lista

    print('Todos os item serão apagados permanentemente.')
    opc = input('Excluir sua To Do List: [s] -- [n] ')

    if opc == 's':
        to_do_list.clear() # --> excluir todos os itens da lista
        menu()

    elif opc == 'n':
        menu()

    else:
        print('Informe uma opção válida.\n')
        clear_to_do_list()


#Menu
def menu():

    print('\n [1] -- Visualizar sua To Do List:  ')
    print(' [2] -- Adicionar item a sua To Do List: ')
    print(' [3] -- Editar item da sua To Do List: ')
    print(' [4] -- Remover item da sua To Do List : ')
    print(' [5] -- Excluir sua To Do List: ')
    print(' [6] -- Sair da sua To Do List: \n')

    opc = input('Entre como uma das opões: ')

    if opc == '1':
        banner('Display', 50, 50)

        display_item()

    elif opc == '2':
        banner('Adicionar item', 50, 50)
        while True:
            opc = input('\nNovo item [s] - [n]? ')
            if opc == 's':
                add_item()
            else:
                menu()
    
    elif opc == '3':
        banner('Editar item', 50, 50)

        edit_item()

    elif opc == '4':
        banner('Remover item', 50, 50)

        remove_item()

    elif opc == '5':
        banner('Limpar Lista', 50, 50)

        clear_to_do_list()
    
    elif opc == '6':
        banner('Sair da To Do List', 50, 50)

        exit()


menu()
        


