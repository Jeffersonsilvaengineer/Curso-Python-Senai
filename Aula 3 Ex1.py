'''Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.'''

def positivo(argumento: float) ->str:
    if argumento >= 0:
        return 'P'
    else:
        return 'N'


print(positivo(float(input('argumento: '))))



