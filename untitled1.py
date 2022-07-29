while True:
while True:
    x=int(input('ingrese el primer numero: '))
    y=int(input('ingrese el segundo numero: '))
    z=input('desea salir')
 
    if x==y:
        print('error los numeros no deben ser igulaes')
    elif x<0 or y<0:
        print('los numeros no deben ser negativos')
    else:
        break