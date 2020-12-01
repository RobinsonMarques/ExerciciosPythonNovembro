#######################################################################################################

# Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, 
# com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. 
# Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

#     8  3  4 
#     1  5  9
#     6  7  2

#     Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. 
# Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. 
# Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3. 

#######################################################################################################

from itertools import permutations

vetores = permutations(range(1, 10), 9)


for i in vetores:
    linha1 = i[0] + i[1] + i[2]
    linha2 = i[3] + i[4] + i[5]
    linha3 = i[6] + i[7] + i[8]
    diagonalP = i[0] + i[4] + i[8]
    diagonalS = i[2] + i[4] + i[6]

    if linha1 == linha2 and linha2 == linha3 and linha3 == diagonalP and diagonalP == diagonalS:
        print(f'{i[0]} {i[1]} {i[2]}')
        print(f'{i[3]} {i[4]} {i[5]}')
        print(f'{i[6]} {i[7]} {i[8]}')
        print('\n')