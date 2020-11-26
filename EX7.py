#######################################################################################################

# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), 
# conte:

#     quantos espaços em branco existem na frase.
#     quantas vezes aparecem as vogais a, e, i, o, u. 


########################################################################################################

string = input('Digite uma frase: ')

list_string = list(string)

espacos = list_string.count(' ')
letras_a = list_string.count('a') + list_string.count('A')
letras_e = list_string.count('e') + list_string.count('E')
letras_i = list_string.count('i') + list_string.count('I')
letras_o = list_string.count('o') + list_string.count('O')
letras_u = list_string.count('u') + list_string.count('U')

print(f'''
Espaços: {espacos}
Letras "A": {letras_a}
Letras "E": {letras_e}
Letras "I": {letras_i}
Letras "O": {letras_o}
Letras "U": {letras_u}
''')
