#Menu opciones
opcion=100

#ciclo/bucle/loop/iteración/SIMON
print("MENU A LA CARTA")
print("*****************")
print("1-->calcular la suma")
print("2-->calcular la resta")
print("3-->calcular la multiplicacion")
print("4-->Calcular la división")
print("0-->SALIR")
print("*****************")
while(opcion!=0):
    opcion=int(input("Digita una opcion: "))
    if(opcion==1):
        numero1=int(input("Digita un numero: "))
        numero2=int(input("Digita otro numero: "))
        print(f'{numero1}+{numero2}={(numero1+numero2)}')
    elif(opcion==2):
        numero1=int(input("Digita un numero: "))
        numero2=int(input("Digita otro numero: "))
        print(f'{numero1}-{numero2}={(numero1-numero2)}')
    elif(opcion==3):
        numero1=int(input("Digita un numero: "))
        numero2=int(input("Digita otro numero: "))
        print(f'{numero1}*{numero2}={(numero1*numero2)}')
    elif(opcion==4):
        numero1=int(input("Digita un numero: "))
        numero2=int(input("Digita otro numero: "))
        print(f'{numero1}/{numero2}={(numero1/numero2)}')
    else:
        print("Digita una opcion valida")

