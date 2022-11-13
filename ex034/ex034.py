#Ex 1080 - Maior e posição

mv = int(input())
pm = 1

for i in range(2, 100+1):
    x = int(input())
    if x > mv:
        mv = x
        pm = i 

print(f'{mv}')
print(f'{pm}')