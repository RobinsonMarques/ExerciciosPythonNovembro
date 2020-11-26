# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#     salário bruto.
#     quanto pagou ao INSS.
#     quanto pagou ao sindicato.
#     o salário líquido.
#     calcule os descontos e o salário líquido, conforme a tabela abaixo: 
#     + Salário Bruto : R$
#     - IR (11%) : R$
#     - INSS (8%) : R$
#     - Sindicato ( 5%) : R$
#     = Salário Liquido : R$

def print_tot(sal_bruto: float, ir: float, inss: float, sindicato: float, sal_liquido: float)-> None:
    print(f'''
Salario Bruto: {sal_bruto}
Imposto de renda (11%): -{ir}
INSS(8%): -{inss}
Sindicato(5%): -{sindicato}
Salário Líquido: {sal_liquido}
''')

def request_data()-> tuple:
    din_hora = float(input('Digite o quanto você ganha por hora: '))
    horas_trab = float(input('Digite o total de horas trabalhadas no mês: '))

    return din_hora, horas_trab

def calc_sal_brute(din_hora: float, horas_trab: float)-> float:
    sal_bruto = din_hora * horas_trab
    return sal_bruto

def calc_discount(sal_bruto: float, tipo: int)-> float:
    if tipo == 1:
        result = sal_bruto * 0.11   
    elif tipo == 2:
        result = sal_bruto * 0.08   
    elif tipo == 3:
        result = sal_bruto * 0.05  
    elif tipo == 4:
        result = sal_bruto - sal_bruto * 0.24
    else:
        print('Tipo inexistente!')
    return result

if __name__ == '__main__':
    data_user = request_data()
    din_hora = data_user[0]
    horas_trab = data_user[1]

    sal_bruto = calc_sal_brute(din_hora, horas_trab)

    ir = calc_discount(sal_bruto, 1)

    inss = calc_discount(sal_bruto, 2)

    sindicato = calc_discount(sal_bruto, 3)

    sal_liquido = calc_discount(sal_bruto, 4)

    print_tot(sal_bruto, ir, inss, sindicato, sal_liquido)
    