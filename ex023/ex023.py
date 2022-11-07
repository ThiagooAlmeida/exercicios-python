#Exercicio 1121 - BeeCrowd - Comprando com desconto

preco_mercadoria = float(input())
quantidade_comprada = int(input())

sem_desconto = preco_mercadoria * quantidade_comprada

desconto_dez = 0.1
desconto_um = quantidade_comprada * 0.01

desconto_total = sem_desconto * (desconto_dez + desconto_um)

com_desconto = sem_desconto - desconto_total

print(f'{sem_desconto:.2f}')
print(f'{com_desconto:.2f}')