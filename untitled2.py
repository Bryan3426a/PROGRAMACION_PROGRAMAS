contador=0
contador_igual=0
contador_negativo=0
while True:
    while True:
        contador+=1
        x=int(input('ingrese el primer numero: '))
         
        y=int(input('ingrese el segundo numero: '))
        
        if x==y:
            print('error los numeros no deben ser igulaes')
             
              contador_igual+=1
        elif x<0 or y<0:
            contador_negativo+=1
            print('los numeros no deben ser negativos')
            
        else:
            break  
         print('las veces que se a ejecutado el codigo es:',contador)
        print('las veces que digitaron numeros iguales es: ',contador_igual)
        print('las veces que digitaron numeros negativos es: ',contador_negativo)
         z=input('para salir digite ,SI: ')
        if z== 'SI' or z=='si' or z=='si' or z=='SI':
             break
    
        