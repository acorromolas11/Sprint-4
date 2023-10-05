import csv
from collections import defaultdict

def verificarFechas(strg):
    return

def verificarValor(strg):
    return

def verificarDNI(strg):
    return

def verificarTipo(strg):
    return

def agregar():
    with open ("cheques.csv","+a",newline='') as salida:
        writer = csv.writer(salida)
        NroCheque = input("Ingrese el NRO de cheque: ")
        CodigoBanco = input("Ingrese el codigo de Banco: ")
        CodigoSucursal = input("Ingrese el codigo de la sucursal: ")
        NumeroCuentaOrigen = input("Ingrese el numero de cuenta de origen: ")
        NumeroCuentaDestino = input("Ingrese el numero de la cuenta de destino: ")
        Valor = input("Ingrese el valor del cheque: ")
        FechaOrigen = input("Ingrese la fecha de origen del cheque: ")
        FechaPago = input("Ingrese la fecha de pago del cheque: ")
        dni = input("Ingrese su numero de DNI: ")
        Estado = input("Ingrese el estado del cheque: ")
        Tipo = input("Ingrese el tipo de cheque: ")
        writer.writerow([NroCheque,CodigoBanco,CodigoSucursal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,dni,Estado,Tipo])
        print("Agregados de manera exitosa")

def menuFiltros():
    print("Seleccione uno de los siguientes filtros: ")
    print("1-Por un DNI particular")
    print("2-Por el tipo de cheque")
    print("3-Estado del cheque")
    print("4-Rango de fechas")

def filtrar():
    menuFiltros()
    print("Filtrado exitoso")

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