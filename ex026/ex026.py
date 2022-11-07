#Exercicio 1165 - BeeCrowd - Doação 

vic_coin = 2.5
doacao = 0
soma_doacao = 0
total_vic_coin = 0

while doacao != -1:
    doacao = float(input())
    
    if doacao != -1:
        soma_doacao += doacao
        total_vic_coin = soma_doacao * vic_coin

print (f'VC$ {soma_doacao:.2f}')
print (f'R$ {total_vic_coin:.2f}')