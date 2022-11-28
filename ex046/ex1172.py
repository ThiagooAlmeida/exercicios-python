#Ex 1172 - Beecrowd - substituição de vetor I

x = [1,2,3,4,5,6,7,8,9,10] #vetor/lista

for i in range(len(x)):# i = posição, i percorrerá todo indice da lista, no caso 10 indices
    x[i] = int(input()) #Numero que ira substituir o valor do indice.
    if x[i] <= 0:#posição de i é menor ou igual a zero?
        x[i] = 1 #se for menor, x[i] receberá o valor 1
        print(f'X{[i]} = {x[i]}')#saida 
