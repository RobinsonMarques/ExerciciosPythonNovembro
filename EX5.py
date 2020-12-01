#######################################################################################################

# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . 
# Depois, mostre quantas vezes cada valor foi conseguido. 
# Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, 
# simulando os lançamentos dos dados. 

#######################################################################################################
import random

cont_list = [0, 0, 0, 0, 0, 0]
numbers = []

def joga_dado()-> None:
    for i in range(100):
        num = random.randrange(1, 7)
        if num == 1:
            cont_list[0] = cont_list[0] + 1
        elif num == 2:
            cont_list[1] = cont_list[1] + 1
        elif num == 3:
            cont_list[2] = cont_list[2] + 1
        elif num == 4:
            cont_list[3] = cont_list[3] + 1
        elif num == 5:
            cont_list[4] = cont_list[4] + 1
        elif num == 6:
            cont_list[5] = cont_list[5] + 1

def print_result()-> None:
    print(f'''
O número 1 foi lançado {cont_list[0]} vezes.
O número 2 foi lançado {cont_list[1]} vezes.
O número 3 foi lançado {cont_list[2]} vezes.
O número 4 foi lançado {cont_list[3]} vezes.
O número 5 foi lançado {cont_list[4]} vezes.
O número 6 foi lançado {cont_list[5]} vezes.
''')

if __name__ == '__main__':
    joga_dado()
    print_result()
    
#Alexandra: meu deus que código lindo :O muito intuitivo de se compreender também, parabainx clap clap 