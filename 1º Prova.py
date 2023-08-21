'''Faça um programa que apresente o menu de opções a seguir, que permita ao usuário escolher a opção desejada,
receba os dados necessários para executar a operação e mostre o resultado. Verificar a possibilidade de opção inválida
 e não se preocupar com as restrições, como salário inválido.
Menu de opções:

1. Novo salário
2. Férias
3. Décimo terceiro
4. Sair

Digite a opção desejada :
Na Opção 1: receber o salário de um funcionário, calcular e mostrar o novo salário usando as regras a seguir.
Salários Percentagem de aumento: Até R$ 350,00 15%, De R$ 350,00 a R$ 600,00 10%, Acima de R$ 600,00 5%.

Na opção 2: receber o salário de um funcionário, calcular e mostrar o valor de suas férias. Sabe-se que as férias
equivalem ao seu salário acrescido de l/2.

Na opção 3: receber o salário de um funcionário e o número de meses de trabalho na empresa, no máximo 12, calcular
 e mostrar o valor do décimo terceiro. Sabe-se que o décimo terceiro equivale ao seu salário multiplicado pelo número
 de meses de trabalho dividido por 12.

Na opção 4: sair do programa.'''

print('-'*30)
print("{:^30}".format("RECURSOS HUMANOS SENAI"))
print('-'*30)
while True:
    opção = int(input('MENU DE OPÇÕES:\n1. Novo salário\n2. Férias\n3. Décimo terceiro\n4. Sair\nESCOLHA UMA OPÇÃO:-->:'))
    while opção not in (1, 2, 3, 4):
        opção = int(input('Opção Inválida!!\n1. Novo salário\n2. Férias \n3. Décimo terceiro\n4. Sair\nESCOLHA UMA OPÇÃO:-->:'))
    if opção == 1:
        salário = float(input('Digite seu salário: '))
        if salário <= 350:
            print(f'Você receberá 15% de aumento, seu novo salário será de R${salário + (salário*(15/100))} reais!')
        elif 350 <= salário <= 600:
            print(f'Você receberá 10% de aumento, seu novo salário será de R${salário + (salário*(10/100))} reais!')
        elif salário > 600:
            print(f'Você receberá 5% de aumento, seu novo salário será de R${salário + (salário * (5/100))} reais!')
    elif opção == 2:
        salário = float(input('Digite seu salário: '))
        print(f'Parabéns! chegou a hora de receber suas férias no valor de {salário + (salário * (50/100))}')
    elif opção == 3:
        salário = float(input('Digite seu salário: '))
        meses = int(input('Quantos mesês você trabalhou este ano: '))
        while not 1 <= meses <= 12:
            meses = int(input('Resposta inválida! escolha um valor entre 1 e 12!: '))
        print(f'Você trabalhou {meses} meses e receberá R${(salário/12)*meses + salário} reais de décimo terceiro!')
    else:
        break
print('FIM!')







