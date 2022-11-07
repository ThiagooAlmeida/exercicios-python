#Exercicio 1126 - BeeCrowd - Dia da entrega - AC1

dia_compra = input()
prazo = int(input())


if dia_compra == "domingo":
    dia_semana = 0
elif dia_compra == "segunda":
    dia_semana = 1
elif dia_compra == "terca":
    dia_semana = 2
elif dia_compra == "quarta":
    dia_semana = 3
elif dia_compra == "quinta":
    dia_semana = 4
elif dia_compra == "sexta":
    dia_semana = 5
elif dia_compra == "sabado":
    dia_semana = 6

dia_entrega = (prazo + dia_semana) % 7 

if prazo == 0:
    print('chega hoje!')
elif dia_entrega == 0:
    print('sera entregue domingo')
elif dia_entrega == 1:
    print('sera entregue segunda')
elif dia_entrega == 2:
    print('sera entregue terca')
elif dia_entrega == 3:
    print('sera entregue quarta')
elif dia_entrega == 4:
    print('sera entregue quinta')
elif dia_entrega == 5:
    print('sera entregue sexta')
elif dia_entrega == 6:
    print('sera entregue sabado')

    
    

