fin = False
print(""" 
      ====Calculadora====
      Menu Pricipal -> Elija una opcion:
      \n1 Suma
      \n2 Resta
      \n3 Producto
      \n4 Division
      \n5 Salir
      """)
while not fin:  
    Opc = int(input("Opcion: "))
    if(Opc == 1):
        suma1 = int(input("Ingrese el primer numero: "))
        suma2 = int(input("Ingrese el segundo numero: "))
        print("La suma es de: ",suma1 + suma2)
    elif(Opc == 2):
        resta1 = int(input("Ingrese el primer numero: "))
        resta2 = int(input("Ingrese el segundo numero: "))
        print("La resta es de: ",resta1 - resta2)
    elif(Opc == 3):
         producto1 = int(input("Ingrese el primer numero: "))
         producto2 = int(input("Ingrese el segundo numero: "))
         print("El producto es de: ",producto1 * producto2)
    elif(Opc == 4):
         division1 = int(input("Ingrese el primer numero: "))
         division2 = int(input("Ingrese el segundo numero: "))
         print("La division es de: ",division1 / division2)
    elif(Opc == 5):
        fin = True