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
numeros = [1, 2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd', 'e']
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




matriz = [[1, 'bruno', 24], [2, 'sla', 12], [3, 'teste', 10]]
# solução 1
# for linha in matriz:
#     for posição, valor in enumerate(linha):
#         if valor == 'sla':
#             linha[posição] = 'Jefferson'
#             break
#     print(linha)


# solução 2
for linha in matriz:
    if 'sla' in linha:
        linha[1] = 'Jefferson'
        break
print(matriz)













































