#Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
numero=str(input('DIGITE VALOR INTEIRO'))
j=len(numero)
l=0
resul=int
for i in range(j):
    l=j-1
    print(f'{numero[l:j]}',end='')
    j-=1
