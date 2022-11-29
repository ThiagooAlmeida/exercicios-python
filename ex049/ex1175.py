#Ex 1175 - beecrowd - Troca de Vetor I
# primeiro código
tam_lista = 20 # tamanho da lista
n = [0]*tam_lista 

for i in range(tam_lista):# i percorrerá o vetor 20 indices - 0 a 19
  n[i] = int(input()) # entrada = vai substituir o valor dos indices
  

pri_pos = 0 #posição no vetor - começando da posição 0
ult_pos = tam_lista -1 #posição no vetor - começando da posição 19

while pri_pos < ult_pos: # enquanto a posição 0 > 19:
  n[pri_pos], n[ult_pos] = n[ult_pos], n[pri_pos] #a posição 0 trocara com a 19
  pri_pos += 1 #atualização das variveis que controlam o laço
  ult_pos -= 1

for i in range(tam_lista): #i vai percorrer toda lista e mostrar o seu valor
  print(f'N[{i}] = {n[i]}')




#segundo código
n = [0]*20 # lista mais seu tamanho

for i in range(20): # i percorrerá toda a lista 0 a 19
    n[i] = int(input()) #n receberá um número que mudara o valor do i (que no caso é a posição da lista)
pos = 0 
for s in n[::-1]: #s percorrerá a lista inteira ("::" significa que s vai ler toda a linha bem como toda coluna, o primeir ":" = linha, o segundo ":" = coluna)
  print(f'N{[pos]} = {s}')
  pos += 1 #atualização da posição