#######################################################################################################

# Faça um programa que gera uma lista dos números primos existentes entre 1 e 
# um número inteiro informado pelo usuário. 

#######################################################################################################



def calc_primo(num: int)-> list:
    lista = []
    for i in range(num):
        cont = 0
        for x in range(i):
            if i % (x+1) == 0:
                cont = cont + 1
        if cont == 2:
           lista.append(x+1)
    return lista

if __name__ == '__main__':
    num = int(input('Digite o número desejado: '))
    primos = calc_primo(num)
    print(*primos)
    