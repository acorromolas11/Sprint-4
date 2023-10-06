import csv
from collections import defaultdict

#-----Extras------

def verificarFechas(strg):
    return

def verificarValor(strg):
    return

def verificarDNI(strg):
    return

def verificarTipo(strg):
    return

def mostrarTitulo():
    print(f"|NroCheque|CodigoBanco|CodigoSucursal|NumeroCuentaOrigen|NumeroCuentaDestino|Valor|FechaOrigen|FechaPago|DNI|Estado|Tipo")

def mostrarDatos(dict):
    print(f"|{dict['NroCheque']}|{dict['CodigoBanco']}|{dict['CodigoSucursal']}|{dict['NumeroCuentaOrigen']}|{dict['NumeroCuentaDestino']}|{dict['Valor']}|{dict['FechaOrigen']}|{dict['FechaPago']}|{dict['DNI']}|{dict['Estado']}|{dict['Tipo']}|")

def crearArchivo(filtro,opcion):
    fieldNames = ["NroCheque","CodigoBanco","CodigoSucursal","NumeroCuentaOrigen","NumeroCuentaDestino","Valor","FechaOrigen","FechaPago","DNI","Estado","Tipo"]
    with open (f"{filtro}_TIMESTAMP_.csv","w",newline='') as wfile:
        with open("cheques.csv","r") as rfile:
            writer = csv.writer(wfile)
            reader = csv.DictReader(rfile)
            writer.writerow(reader.fieldnames)
            for row in reader:
                if(row["DNI"]==filtro and opcion==1):
                    writer.writerow(row.values())
                elif(row["Tipo"]==filtro and opcion==2):
                    writer.writerow(row.values())
                elif(row["Estado"]==filtro and opcion==3):
                    writer.writerow(row.values())

def crearArchivoFechas(strg1,strg2):
    fieldNames = ["NroCheque","CodigoBanco","CodigoSucursal","NumeroCuentaOrigen","NumeroCuentaDestino","Valor","FechaOrigen","FechaPago","DNI","Estado","Tipo"]
    with open (f"FECHAS_TIMESTAMP_.csv","w",newline='') as wfile:
        with open("cheques.csv","r") as rfile:
            writer = csv.writer(wfile)
            reader = csv.DictReader(rfile)
            writer.writerow(reader.fieldnames)
            for row in reader:
                if(strg1<row["FechaOrigen"]<strg2):
                    writer.writerow(row.values)

#----Agregar---------

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

#----Fin Agregar----------

#----Inicio Filtrado--------

def filtrado(filtro,opcion,salida):
    if(salida == 1):
        with open("cheques.csv","r") as file:
            reader = csv.DictReader(file)
            if(salida == 1):
                mostrarTitulo()
                for row in reader:
                    if(row["DNI"]==filtro and opcion==1):
                        mostrarDatos(row)
                    elif(row["Tipo"]==filtro and opcion==2):
                        mostrarDatos(row)
                    elif(row["Estado"]==filtro and opcion==3):
                        mostrarDatos(row)
    elif(salida == 2):
        crearArchivo(filtro,opcion)
                

def filtradoFechas(strg1,strg2,salida):
    if(salida==1):
        with open("cheques.csv","r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if(strg1<row["FechaOrigen"]<strg2):
                    mostrarDatos(row)
    elif(salida==2):
        crearArchivoFechas(strg1,strg2)

                

def menuFiltros():
    opcion = 0
    strg = ""
    strg1 = ""
    strg2 = ""
    salida = int(input("Ingrese '1' si desea una salida por pantalla o '2' si la desea creando un archivo csv: "))
    while(opcion>0 or opcion<=4):
        print("Seleccione uno de los siguientes filtros: ")
        print("1-Por un DNI particular")
        print("2-Por el tipo de cheque")
        print("3-Estado del cheque")
        print("4-Rango de fechas")
        print("5-Salir")
        opcion = int(input())
        if(opcion==1):
            strg = input("Ingrese el DNI a filtrar: ")
            filtrado(strg,opcion,salida)
        elif(opcion==2):
            strg = input("Ingrese el tipo de cheque: ")
            filtrado(strg,opcion,salida)
        elif(opcion==3):
            strg = input("Ingrese el estado del cheque: ")
            filtrado(strg,opcion,salida)
        elif(opcion==4):
            strg1 = input("Ingrese la primera fecha: ")
            strg2 = input("Ingrese la segunda fecha: ")
            filtradoFechas(strg1,strg2,salida)
        elif(opcion==5):
            break
        else:
            print("Ingrese una opción valida!")

def filtrar():
    menuFiltros()
    print("Filtrado exitoso")

#----Fin Filtrado----

#---Inicio Salir

def salir():
    print("Fin")

#----Fin salir----

#---Inicio Menu----

def menu():
    opcion = 0
    while(opcion>0 or opcion<=3):
        print("Bienvenido al menu")
        print("1-Agregar")
        print("2-Filtrar")
        print("3-Salir")
        opcion = int(input("Elija una opción: "))
        if(opcion==1):
            agregar()
        elif(opcion==2):
            filtrar()
        elif(opcion==3):
            salir()
            break
        else:
            print("La opción ingresada no es valida, ingrese una opción válida")

#-----Fin Menu-----


#----MAIN------
menu()
#----FIN MAIN-----