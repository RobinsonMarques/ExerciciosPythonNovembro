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

#Alexandra: e pra finalizar o segundo exercício mais fácil, muito bommm :3 de conselho pra simplificar entre a
#linha 17 e 21 é usar o comando .lower, ele torna uma letra como mesma variável independente de estar maiúscula
#e minúscula :] assim:
# vogais = 'a e i o u'
# str = str.lower() 
#porém o seu continua ótimo e intuitivo :D