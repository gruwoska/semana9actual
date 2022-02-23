import listas as lis
import pilas as pil
import colas as col
import os
def borrar():
     os.system("cls")
     
opcion=0
while opcion!=4:
    borrar()
    print("--Ingrese 1 para ingresar al Menú de Lista--\n--Ingrese 2 para ingresar al Menú de Pilas--\n--Ingrese 3 para ingresar al Menú de Colas--\n--Ingrese 4 para salir del programa-")
    opcion=int(input("Elija la Opción:"))
    if opcion==1:
        borrar()
        opcion1=0
        while opcion1!=7:
            print("Menú de Lista:\n  1) push \n  2) pop \n  3) show \n  4) eliminar \n  5) insertar \n  6) buscar \n  7) salir")
            opcion1=int(input("Elija la Opción:"))
        pass
    elif opcion==2:
        borrar()
        opcion2=0
        while opcion2!=6:
            print("Menú de Pila:\n  1) push \n  2) pop \n  3) show \n  4) buscar \n  5) Longitud \n  6)Salir")
            opcion2=int(input("Elija la Opción:"))
        pass
    elif opcion==3:
        borrar()
        opcion3=0
        while opcion3!=4:
            print("Menú de Colas:\n  1)añadir \n  2)sacar \n  3) pshow \n  4) salir ")
            opcion3=int(input("Elija la Opción:"))
    elif opcion==4:
        print("Saliendo del programa")
        
