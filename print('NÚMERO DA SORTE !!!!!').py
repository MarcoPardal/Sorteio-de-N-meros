print('NÚMERO DA SORTE !!!!!')

print('')

import random


def sortear_numeros(qtd=6,minimo=1,maximo=60):
    numeros_sorteados= random.sample (range(minimo, maximo+1),qtd)
    return sorted(numeros_sorteados)
numeros = sortear_numeros()
print("Números para o sorteio da Mega-Sena:",numeros)
print('***ATENÇÃO*****')
print('Este aplivativo não vale como sorteio oficial da Mega-Sena.')