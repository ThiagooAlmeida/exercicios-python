#Ex 1073 - Beecrowd - Quadrado de pares


n = int(input())


for i in range(1, n+1):
    if i % 2 == 0:
        print(f'{i}^2 = {i**2}')
