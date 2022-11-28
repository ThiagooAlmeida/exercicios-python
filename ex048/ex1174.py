#Ex 1174 - Beecrowd - Seleção em Vetor I

a = [] #vetor sem qtd de indice.

#obs pessoal: nunca colocar "a = [valor]" pq o exercicio não pede para analisar os indices, só mostrar a qtd de itens que n percorrerá.

for i in range(100): # i percorrera de 0 a 99, não usar a função len pois no exercicio não ha pq analisar os indices da lista

  n = float(input())# numero que vai ser analisado
  a.append(n)#numero digitado vai ser inclementado na lista
  if n <= 10.0:# o numero digitado é menor ou igual a 10?
    print(f'A{[i]} = {n}')