# Ex 1165 - Beecrowd - Número primo

#Código não está funcionando na plataforma :(
def eh_primo(n):
    y = 2
    while y < n//2 + 1:
        if n % y == 0:
            return False
        y += 1 
    return True


qtd_testes = int(input())

cont = 1

while cont < qtd_testes: 
    x = int(input())
    if eh_primo(x):
        print (f'{x} eh primo')
     
    else:
        print (f'{x} nao eh primo')
        cont += 1 


#2o código que não funciona no beecrowd

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