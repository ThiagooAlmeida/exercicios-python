#Exercicio 1065 - BeeCrowd - Pares entre cinco números

num_pares = 0
for n in range(5):
    num = int(input())
    if(num % 2 == 0):
        num_pares = num_pares + 1
print('%i valores pares'%num_pares)       
