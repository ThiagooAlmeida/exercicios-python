#Exercicio 1067 - BeeCrowd - Números impares

#Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o caso.

#Entrada
#O arquivo de entrada contém 1 valor inteiro qualquer.

#Imprima todos os valores ímpares de 1 até X, inclusive X, se for o caso.

valor = int(input())

#x = 1 

#while x <= valor:
  #  print(x)
   ## x+=2


for i in range(1,valor+1,2):
    print(i)


