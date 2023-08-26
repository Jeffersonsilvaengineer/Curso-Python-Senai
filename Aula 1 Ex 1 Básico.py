'''1) Uma imobiliária vende apenas terrenos retangulares. Faça um algoritmo para ler as dimensões de um
terreno e depois exibir a área do terreno.'''

largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))
while comprimento <= largura:
    print('Desculpe está medida é inválida!')
    largura = float(input('Digite a largura do terreno: '))
    comprimento = float(input('Digite o comprimento do terreno: '))
area = largura * comprimento
print(f'A área total do terreno é {area} metros quadrados!')


