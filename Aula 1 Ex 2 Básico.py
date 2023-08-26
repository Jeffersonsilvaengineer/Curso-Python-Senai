'''2) Um posto pensando na comodidade para seus clientes deseja disponibilizar uma busca prévia para os clientes que
pretendem abastecer. Escreva um algoritmo para ler o preço do litro da gasolina e o valor do pagamento,
e exibir quantos litros ele conseguiria abastecer.'''

preço = float(input('Qual o preço do litro de gasolina: '))
valor = float(input('Qual o valor a ser pago pelo abastecimento: '))
litros = valor / preço
print(f'Com o valor de {valor} reais você está colocando {litros} litros de gasolina no seu carro!')
