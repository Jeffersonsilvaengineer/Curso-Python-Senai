'''3) Um rancho deseja automatizar o seus pedidos de compra do mês de ração para seus cavalos. Sabendo que cada cavalo
come por dia 1,2 Kg de ração, o usuário deve informar quantos cavalos precisam de ração e o sistema deve devolver a
quantidade que deve ser comprada.'''

dia = 1.2
mes = 30
cavalos = float(input('Quantos cavalos precisan de ração: '))
print(f'São {cavalos} cavalos, será necessário compar {(cavalos*dia)*mes:.2f} kilos de ração para dar para todo o mês')
