# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 12:30:00 2022

@author: Acer
"""

litro_kilómetros = float(input("Introduzca el valor de litros / kilómetros: "))
millasp_galon= float(input('Ingrese el valor de millas por galon: '))

milla_americana = 1609.344
galon_americano=3.785411784 

mpg= litro_kilómetros * galon_americano
lkpg= millasp_galon * milla_americana

print('%0.2f litros / kilómetros es igual a %0.2f millas por galon' %(litro_kilómetros, mpg))
print('%0.2f millas por galon es igual a %0.2f litro / kilometros' %(millasp_galon, lkpg))