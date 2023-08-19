'''Uma loja registra as vendas em seu sistema inserindo o valor da venda e o código da transação. O código de
transação 'v' para vendas à vista e 'p' para parceladas. Faça um programa que receba o valor e o códig de 15 vendas
usando laço de repetição for e mostre:
O valor total das vendas a vista!
O valor total das vendas parceladas!'''
vista = []
parcelado = []

for c in range(0, 15):
    vendas = float(input(f'Digite o valor da {c}º venda: '))
    código = input(f'Qual o código da operação da {c}º venda: ')
    if código == "v":
        vista.append(vendas)
    else:
        parcelado.append(vendas)
print(f'Você teve {len(vista)} vendas à vista, com o valor total de {sum(vista)}!')
print(f'Você teve {len(parcelado)} vendas parceladas, com o valor total de {sum(parcelado)}!')
