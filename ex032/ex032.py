#Ex 1154 - BeeCrowd - Idades

soma = 0 
qtd = 0 

while True:
    idade = int(input())
    if idade < 0:
        break
    else:
        soma += idade
        qtd += 1

print(f'{soma/qtd:.2f}')

'''
Exemplo de entrada - beecrowd:
34
56
44
23
-2
'''
