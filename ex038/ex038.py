#Ex 1164 - Beecrowd - Número perfeito 

def eh_perfeito(n):
    x = 0
    for i in range(1, n):
        if n % i == 0:
            x += i
    
    if x == n:
        return True
    else:
        return False
    

qtd_teste = int(input())
cont = 0

while cont < qtd_teste:
    x = int(input())
    if eh_perfeito(x):
        print(f'{x} eh perfeito')
    else:
        print(f'{x} nao eh perfeito')

    cont +=1
