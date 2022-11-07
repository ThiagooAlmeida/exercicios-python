#Exercicio 1012 - beecrowd - Área 

a,b,c = map(float, input().split())
r1 = a*c/2
r2 = 3.14159*(c ** 2)
r3 = c *(a + b) / 2
r4 = b * b 
r5 = a * b

print('TRIANGULO: %.3f'%r1)
print('CIRCULO: %.3f'%r2)
print('TRAPEZIO: %.3f'%r3)
print('QUADRADO: %.3f'%r4)
print('RETANGULO: %.3f'%r5)
