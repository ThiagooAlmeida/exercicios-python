#Ex 3037 - Beecrowd - Jogando Dardos por distancia

qtd = int(input())

for i in range(qtd): #qtd de vezes que o laço vai repetir.
    pj = 0 # Variavel acumuladora do laço 2º for
    for j in range(3): #repetir 3x 
        x, d = input().split()
        x, d = int(x), int(d)
        pj += x*d

    pm = 0
    for j in range(3):
        x, d = input().split()
        x, d = int(x), int(d)
        pm += x*d

    if pm > pj:
        print('MARIA')
    else:
        print('JOAO')