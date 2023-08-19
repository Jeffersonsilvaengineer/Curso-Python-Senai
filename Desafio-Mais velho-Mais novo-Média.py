'''Crie um programa que receba a idade de 10 pessoas e retorne, o mais novo, o mais velho e a média de idade.'''

# 1º solução

idade = []
cont = 0
while True:
    cont += 1
    idade.append(int(input(f'Digite a {cont}º idade: ')))
    continuar = input('Quer continuar [SIM/NÃO]').upper()
    if continuar =='NÃO':
        break
print(f'A menor idade é {min(idade)}')
print(f'A maior idade é {max(idade)}')
print(f'A média de idades é {sum(idade)/len(idade)}')


# 2º solução

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
maior = lista[0]
menor = lista[0]
media = 0
for n in lista:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    media += n
print(f'A menor idade é {menor}')
print(f'A maior idade é {maior}')
print(f'A média de idades é {media/len(lista)}')
