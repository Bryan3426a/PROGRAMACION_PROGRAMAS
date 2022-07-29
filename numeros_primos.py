# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 12:02:44 2022

@author: Acer
"""

n = 0
cont=0
sum=0
while n < 1:
    n= int(input(' Ingrese un valor: '))
    print()
    if n<=0:
        print(' El numero debe ser mayor a 0')
        
for i in range(2, n+1): 
  if i>1: 
    for j in range(2,i): 
            if((i % j)==0):
                break              
    else: 
        print(str(i)+ ' =Es primo')
        cont=cont+1
        sum=sum+i
print('-------------------------------------------')
print(str(cont)+'->Numeros son primos')
