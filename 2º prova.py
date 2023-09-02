'''Crie um programa que permita aos usuários gerenciarem suas tarefas usando um lista de afazeres ("to-do list").
O programa deve oferecer as seguintes funcionalidades:
1) Adcionar uma tarefa à lista
2) Visualizar todas as tarefas na lista
3) Marcar uma tarefa como concluida
4) Remover uma tarefa da lista
5) Sair do programa

orientações:
Crie o 'menu de opções' como uma tupla;
Crie as tarefa como dicionários; '''
lista = []
while True:
    opção = int(input('MENU DE OPÇÕES:\n'
                      '1. Adcionar uma tarefa à lista\n'
                      '2. Visualizar todas as tarefas na lista\n'
                      '3. Marcar uma tarefa como concluida\n'
                      '4. Remover uma tarefa da lista\n'
                      '5. Sair\n'
                      'ESCOLHA UMA OPÇÃO:-->:'))
    while opção not in (1, 2, 3, 4, 5):
        opção = int(input('Opção Inválida!!\n'
                          '1. Adcionar uma tarefa à lista\n'
                          '2. Visualizar todas as tarefas na lista\n'
                          '3. Marcar uma tarefa como concluida\n'
                          '4. Remover uma tarefa da lista\n'
                          '5. Sair\n'
                          'ESCOLHA UMA OPÇÃO:-->:'))
    if opção == 1:
        print('Vamos adcionar nova tarefa!')
        novatarefa = dict["Nova tarefa "] = str(input('Digite a tarefa: '))
    elif opção == 2:
        print('Aqui estão todas as tarefas!')
        print(dict)
    elif opção == 3:
        print('Vamos marcar uma tarefa como concluida!')
    elif opção == 4:
        remover = dict
    elif opção == 5:
        break
print(dict)























































