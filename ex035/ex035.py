#Ex 1546 - beecrowd - Feedback

q = int(input())#qtd de testes 
for i in range(q):
    membros = int(input())
    for s in range(membros):
        n = int(input())
        if n == 1: print('Rolien')
        elif n == 2: print('Naej')
        elif n == 3: print('Elehcim')
        else: print('Odranoel')

'''
Entradas:
2
4
1
1
3
4
3
3
3
2


saida:
Rolien
Rolien
Elehcim
Odranoel
Elehcim
Elehcim
Naej
'''