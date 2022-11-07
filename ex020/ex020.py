#Exercicio 1124 - beecrowd - Jogo do par ou impar

n = int(input())

if n % 2 == 0:
    impar_antecessor = n - 1
    par_sucessor = n + 2 

else:
    impar_antecessor = n - 2 
    par_sucessor = n + 1

print(f'{impar_antecessor} {par_sucessor}')