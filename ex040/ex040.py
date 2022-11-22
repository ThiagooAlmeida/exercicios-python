#Ex 1285 - Beecrowd - Digitos Diferentes

while True:
    try:
        n, m = input().split()
        x = 0 #qtd de digitos não repetidos entre os intervalos
            # N/M
        for i in range(int(n),int(m)+1):
            if len(set(list(str(i)))) == len(str(i)):
                x += 1
        print(f'{x}')

    except:
        break