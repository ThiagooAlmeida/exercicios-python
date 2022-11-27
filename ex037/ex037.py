# Ex 1165 - Beecrowd - Número primo


def eh_primo(n):
    y = 2 #começando do n2 pq o 1 é smp divisor
    while y < n//2 + 1: # Varivel y irá percorrer até a 1/2 + 1 e parar
        if n % y == 0:
            return False
        y += 1
    return True
    

qtd_testes = int(input())

cont_primos = 0 
for _ in range(qtd_testes):
    x = int(input())
    if eh_primo(x):
        print(f'{x} eh primo')
        cont_primos += 1
    else:
        print(f'{x} nao eh primo')




# código que não funciona no beecrowd

qtd_testes = int(input())

for i in range(0, qtd_testes+1):
    n = int(input())
    s = 0 #Variavel de soma
    j = 1 #Posição na lista/controladora
    
    while j <= n:
        if n % j == 0:
            s += 1
        j += 1
    if s > 2:
        print(f'{n} nao eh primo')
    else:
        print(f'{n} eh primo')