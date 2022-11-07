#Exercicio 1009 - Beecrowd - Salário com bonus 

nome = str(input())
sal_fixo = float(input())
vendas = float(input())
sal_bonus = sal_fixo + (vendas * 0.15)

print(f'TOTAL = R$ {sal_bonus:.2f}')
