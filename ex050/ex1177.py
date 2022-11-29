#Ex 1177 - Preenchimento de Vetor II 

valor = int(input()) 
n = [0]*1000 #tamanho da lista

for i in range(1000):
  n[i] = i%valor #posição de "i" vai ser o resto da divisão de "i" e valor recebido (no Ex: 3 % 0 = 0 e assim por diante)
  
for i in range(1000): #i percorrerá até 999 e mostrará o valor
  print(f'N[{i}] = {n[i]}')