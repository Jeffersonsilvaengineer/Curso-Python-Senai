# for i in range(3):
#     senha = int(input('Digite a senha: '))
#     if senha == 123:
#         print('Bem vindo!')
#         break
#     else:
#         print('Senha incorreta!')

# for c in range(1, 5):
#     if c == 3:
#         continue
#     print(c)
#
# for c in range(1, 5):
#     if c == 3:
#         pass
#     print(c)
#
# for c in range(1, 5):
#     if c == 3:
#         break
#     print(c)
#
# lista = ['a', 'b', 'c', 'd', 'e']
#
# for posição, valor in enumerate(lista):
#     if valor == 'd':
#         lista[posição] = 'olá'
# print(lista)
#
#
# numeros = [1, 2, 3, 4, 5]
# letras = ['a', 'b', 'c', 'd', 'e']
# print(type(numeros))
# print(type(letras))
# numeros[1] = 200
# print(numeros)
# for n in numeros:
#     print(n)
# for posição, valor in enumerate(numeros):
#     if valor == 4:
#         numeros[posição] = 12
#     print(f'posição:{posição} valor:{valor}')

#
# if 4 in numeros:
#     print('Tem!')
#
#
# numeros.append(30) # adiciona no final da lista
# print(numeros)
# numeros.pop(2) # remove a posição especifica
# print(numeros)
# numeros.insert(0, 30) # adiciona na posição especifica
# print(numeros)
# numeros = [1, 2, 3, 4, 5]
# for posição, valor in enumerate(numeros):
#     if valor == 4:
#         numeros.insert(posição, 'palavra')
#         break
# print(numeros)




# matriz = [[1, 'bruno', 24], [2, 'sla', 12], [3, 'teste', 10]]
# solução 1
# for linha in matriz:
#     for posição, valor in enumerate(linha):
#         if valor == 'sla':
#             linha[posição] = 'Jefferson'
#             break
#     print(linha)


# solução 2
# for linha in matriz:
#     if 'sla' in linha:
#         linha[1] = 'Jefferson'
#         break
# print(matriz)


matriz = [{
    "codigo": 1,
    "nome": "Bruno",
    "idade": 24
},
    {"codigo": 2,
    "nome": "André",
    "idade": 12
},

    {"codigo": 3,
    "nome": "Maria",
    "idade": 18
}]
for registro in matriz:
    if 'André' in registro["nome"]:
        registro["nome"] = 'jefferson'
        break
print(matriz)

print('+++++++++++++++++ TO-DO-LIST  +++++++++++++++++')
print('Digite uma opção abaixo')

menu = (' 1 Adicionar uma nova atividade', ' 2 Vizualizar uma tarefa', ' 3 Finalizar uma tarefa', ' 4 Remover Tarafa',
        ' 5 Sair do Programa')

tarefas = []

for i, option in enumerate(menu):
    print(option)

while True:
    escolha = int(input('--->Digite aqui a opção desejada:'))
    if escolha == 1:
        descricao = str(input('Digite sua nova tarefa '))
        novatarefa = {
            "descrição": descricao,
            "concluido": "Não"
        }
        tarefas.append(novatarefa)

        print(f'Sua nova tarefa foi adicionda com sucesso! \n ****Veja o que há de registro*** \n {tarefas}')

    elif escolha == 2:
        print(f'Suas atividade até o momento são \n {tarefas}')

    elif escolha == 3:
        print(tarefas)
        print('----Veja suas tarefas acima e qual sera concluida!----')
        ok = str(input('Digite qual das terafas a cima sera concluida '))
        for tarefa in tarefas:
            if tarefa["descrição"] == ok:
                tarefa["concluido"] = "Sim"
                print('Alterado!!')


    elif escolha == 4:
        print(tarefas)
        print('----Veja suas tarefas acima e qual sera removida!----')
        remover = str(input('Digite qual das terafas a cima sera removida '))

        for valor, tarefa in enumerate(tarefas):
            if tarefa["descrição"] == remover:
                tarefas.pop(valor)
                print(f'{remover} foi emovido com Sucesso!')



    elif escolha == 5:
        print('Finalizando To-do-List! :)')
        break

    else:
        print('Nenhuma opção valida, escolha uma opção valida de 1 a 5!')



























