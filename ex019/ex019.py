#Exercicio 1125 - BeeCrowd - Professor, mas é só 0,5



notaAtividade = float(input())
notaProva = float(input())

mediaFinal = (notaAtividade+notaProva) / 2

if mediaFinal >= 6:
    print('aprovado')
elif mediaFinal < 6 and notaAtividade >= 2:
    print('talvez com a sub')
else:
    print ('reprovado')

