#Ex 1173 - Beecrowd - preenchimento de Vetor I

v = int (input())#recebe o número (Ex = 1)

for i in range(10): #i percorrerá 10 indices, ou seja, de 0 a 9
  print(f'N{[i]} = {v}')
  v*=2 # atualizando do valor de V, multicaplicação por 2 