sair = False
clientes = []

def Crud(opcao, nome = '', idade = 0, id = 0):
    global clientes, sair
    if opcao == 1:
        contador = (len(clientes) + 1)
        cliente = {
            'id': contador,
            'nome': nome,
            'idade': idade
        }
        clientes.append(cliente)
        if input('Sair? y/n: ') == 'y':
            sair = True
    if opcao == 2:
        print(clientes)
        if input('Sair? y/n: ') == 'y':
            sair = True


while not sair:
    opcao = int(input('Opcao: '))
    if opcao != 2:
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        Crud(opcao, nome, idade)
    else:
        Crud(opcao)