# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 18:53:35 2022

@author: S7
"""

num=int(input('Ingrese un numero:'))
def NumeroPrimo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo")
            return False
        if num%n!=0:
            print("Es primo")
            return True
print(NumeroPrimo(num))