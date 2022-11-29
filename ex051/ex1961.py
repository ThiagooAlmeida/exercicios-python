#Ex 1961 - beecrowd - Pula Sapo


def jogar(pulo, n , canos):
    for i in range(1, n):
        if abs(canos[i] - canos[i-1]) > pulo:
            return False
    return True


pulo, n = map(int,input().split())#Pulo = 5, n = 10
canos = [int(x) for x in input().split()]#1 3 6 9 7 2 4 5 8 3

if jogar(pulo, n, canos):
    print('YOU WIN')
else:
    print('GAME OVER')