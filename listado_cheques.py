import csv
from collections import defaultdict

def agregar():
    print("Agrego")

def filtrar():
    print("Filtro")

def exportar():
    print("Exporto")

def salir():
    print("Fin")

def menu():
    opcion = 0
    while(opcion>0 or opcion<=4):
        print("Bienvenido al menu")
        print("1-Agregar")
        print("2-Filtrar")
        print("3-Exportar")
        print("4-Salir")
        opcion = int(input("Elija una opción: "))
        if(opcion==1):
            agregar()
        elif(opcion==2):
            filtrar()
        elif(opcion==3):
            exportar()
        elif(opcion==4):
            salir()
            break
        else:
            print("La opción ingresada no es valida, ingrese una opción válida")


menu()

#Agregar
#Filtrar
#Exportar
#Salir