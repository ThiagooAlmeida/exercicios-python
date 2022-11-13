#Ex 1153 - beecrowd - Fatorial simples

n = int(input())

soma_fatorial = 1

for i in range(1, n+1):
    soma_fatorial *= i

print (f'{soma_fatorial}')

