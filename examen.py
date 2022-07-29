'A continuación, se van solicitando números hasta que se introduzca el 0'
'Al finalizar el programa debe imprimir la siguiente información:'
#a)       La suma de los números que están dentro del intervalo.

#b)      El promedio de números ingresados que están fuera del intervalo.

#c)       La cantidad de números que fueron iguales a los límites del intervalo.
contador_igual=0
while True:
    val1=int(input('ingrese el primer valor: '))
    val2=int(input('ingrese el segundo valor: '))
    
    intervalos_fuera=[]
    intervalos_dentro=range(1,10+1)
    if val1==val2 or val2==val1:
        print('los valores son iguales')
        contador_igual+=1
    
    for intem in intervalos_dentro:      
            for item in range(10):
                print(intem)  
            else:
                val1_2=val1+val2
                suma=(intervalos_dentro+val1_2)/2
                promedio=(suma+intervalos_dentro+intervalos_fuera)/2               
                print('La suma de los números que están dentro del intervalo',suma)
                print('El promedio de números ingresados que están fuera del intervalo',promedio)
                print('La cantidad de números que fueron iguales a los límites del interval',contador_igual)


    

