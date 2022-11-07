#Exercicio 1167 - Beecrowd - Anos bissextos

inicio = int(input())
fim = int(input())
qtd_bissexto = 0

# LOGICA
if (0 <= inicio <= fim <= 9999):
  while inicio <= fim:
    if (inicio % 4 == 0 and inicio % 100 != 0 or inicio % 400 == 0):
      print(inicio)
      qtd_bissexto += 1
    
    inicio += 1
  
  print(f'bissextos: {qtd_bissexto}')


 






