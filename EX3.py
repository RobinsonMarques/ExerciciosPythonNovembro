####################################################################################################### 

# Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. 

#######################################################################################################

def ver_tri(ladoa: float, ladob: float, ladoc: float) -> str:
    if ladoa > 0 and ladob > 0 and ladoc > 0:
        if ladoa + ladob > ladoc or ladoc + ladoa > ladob or ladob + ladoc > ladoa:
            if ladoa == ladob and ladob == ladoc:
                result = 'Triângulo Equilátero'
            elif ladoa == ladob or ladob == ladoc or ladoc == ladoa:
                result = 'Triângulo Isósceles'
            else:
                result = 'Triângulo Escaleno'
        else:
            result = 'Os lados informados não formam um triângulo'
    else:
        result = 'Número informado negativo!'
    return result

if __name__ == "__main__":
    ladoa = float(input('Digite o lado A do triângulo: '))
    ladob = float(input('Digite o lado B do triângulo: '))
    ladoc = float(input('Digite o lado C do triângulo: '))
    tipo = ver_tri(ladoa, ladob, ladoc)
    print(tipo)
