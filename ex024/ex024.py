#AC2 - Exercicio 1166 - BeeCrowd - Pague o aluguel! 

#14 meses de atraso

divida = int(input())
pag_mensal = int(input())

qtd_pag = 0

while divida != 0:
    qtd_pag += 1

    print (f'pagamento: {qtd_pag}')
    print (f'antes = {divida}')
    divida = divida - pag_mensal
    print(f'depois = {divida}')
    if divida < 0:
        divida = 0 
    print('-----')
      
#Resolução aceita no Beecrowd      
divida = int(input())
pag_mensal = int(input())
contador = 0

while divida != 0:
    contador += 1

    if divida >= pag_mensal:
        antes = divida
        divida = divida - pag_mensal
        depois = divida
    else:
        antes = divida
        divida = divida - divida
        depois = divida

    print(f'pagamento: {contador}')
    print(f'antes = {antes}')
    print(f'depois = {depois}')
    print('-----')