######################################################################################################

# Faça um Programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em 
# latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#     Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#     comprar apenas latas de 18 litros;
#     comprar apenas galões de 3,6 litros;
#     misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
# 

#######################################################################################################

import math

tam = float(input('Digite o tamanho da área a ser pintada (em metros quadrados): '))
tot_lit_tinta = (tam / 6) * 1.10

latas = math.ceil(tot_lit_tinta / 18)
gal = math.ceil(tot_lit_tinta / 3.6)
pagar_latas = latas * 80
pagar_gal = gal * 25

if tot_lit_tinta > 18:
    latas2 = tot_lit_tinta // 18
    aux = tot_lit_tinta % 18
    gal2 = math.ceil(aux / 3.6)
    pag_lat_gal = latas2 * 80 + gal2 * 25 
else:
    latas2 = 0
    gal2 = gal
    pag_lat_gal = pagar_gal

print(f'''
###Latas###
Quantidade: {latas}
Total a pagar: {pagar_latas}

###Galões###
Quantidade: {gal}
Total a pagar: {pagar_gal}

###Latas e Galões###
Quantidade Latas: {latas2}
Quantidade Galões: {gal2}
Total a pagar: {pag_lat_gal}
''')
