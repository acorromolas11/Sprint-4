import csv
from collections import defaultdict
import datetime

#-----Extras------

def ingresarGenerico(strg):
    return int(input(strg))

def verificarDNI(strg):
    ver = int(input(strg))
    while(ver>99999999 or ver<10000000):
        print("Valor invalido!")
        ver = int(input(strg))
    return ver

def verificarValor(strg):
    return float(input(strg))

def verificarFechas(strg):
    print(strg)
    
    año = int(input("Ingrese el año: "))
    while (año<=0):
        print("Año invalido!")
        año = int(input("Ingrese el año: "))
    
    mes = int(input("Ingrese el mes: "))
    while (mes<=0 or 13<=mes):
        print("Mes invalido!")
        mes = int(input("Ingrese el mes: "))
    
    dia = int(input("Ingrese el día: "))
    if(mes==1 or mes==3 or mes==5 or mes==7 or mes==9 or mes==11):
        ultimo=31
    elif(mes==4 or mes==6 or mes==8 or mes==10 or mes==12):
        ultimo=30
    else:
        ultimo=29

    while(dia<=0 or ultimo<dia):
        print("Dia invalido!")
        dia = int(input("Ingrese el día: "))

        
    fecha = datetime.datetime(año,mes,dia)
    return fecha.strftime("%Y-%m-%d")

def verificarTipo(strg):
    ver = input(strg)
    while(ver.lower()!="depositado" and ver.lower()!="emitido"):
        print("Valor invalido, los tipos de cheques son 'depositado' o 'emitido'")
        ver = input(strg)
    return ver

def verificarEstado(strg):
    ver = input(strg)
    while(ver.lower()!="aprobado" and ver.lower()!="pendiente" and ver.lower()!="rechazado"):
        print("Valor invalido, los estados de cheques son 'aprobado','pendiente' o 'rechazado'")
        ver = input(strg)
    return ver

def mostrarTitulo():
    print(f"|NroCheque|CodigoBanco|CodigoSucursal|NumeroCuentaOrigen|NumeroCuentaDestino|Valor|FechaOrigen|FechaPago|DNI|Estado|Tipo")

def mostrarDatos(dict):
    print(f"|{dict['NroCheque']}|{dict['CodigoBanco']}|{dict['CodigoSucursal']}|{dict['NumeroCuentaOrigen']}|{dict['NumeroCuentaDestino']}|{dict['Valor']}|{dict['FechaOrigen']}|{dict['FechaPago']}|{dict['DNI']}|{dict['Estado']}|{dict['Tipo']}|")

def crearArchivo(filtro,opcion):
    with open (f"{filtro}_{datetime.datetime.now().strftime('%Y-%m-%d')}_.csv","w",newline='') as wfile:
        with open("cheques.csv","r") as rfile:
            writer = csv.writer(wfile)
            reader = csv.DictReader(rfile)
            writer.writerow(reader.fieldnames)
            for row in reader:
                if(row["DNI"]==filtro and opcion==1):
                    writer.writerows(row.values())
                elif(row["Tipo"]==filtro and opcion==2):
                    writer.writerows(row.values())
                elif(row["Estado"]==filtro and opcion==3):
                    writer.writerows(row.values())

def crearArchivoFechas(strg1,strg2):
    fieldNames = ["NroCheque","CodigoBanco","CodigoSucursal","NumeroCuentaOrigen","NumeroCuentaDestino","Valor","FechaOrigen","FechaPago","DNI","Estado","Tipo"]
    with open (f"FECHAS_{datetime.datetime.now().strftime('%Y-%m-%d')}_.csv","w",newline='') as wfile:
        with open("cheques.csv","r") as rfile:
            writer = csv.writer(wfile)
            reader = csv.DictReader(rfile)
            writer.writerow(reader.fieldnames)
            for row in reader:
                if(strg1<row["FechaOrigen"]<strg2):
                    writer.writerow(row.values)

#----Agregar---------

def agregar():
    with open ("cheques.csv","r") as lectura:
        reader = csv.reader(lectura)
        for row in reader:
            ultimo = row[0]
        ultimo = int(ultimo)
    with open ("cheques.csv","+a",newline='') as salida:
        writer = csv.writer(salida)
        NroCheque = ultimo + 1 
        #NroCheque = ingresarGenerico("Ingrese el NRO de cheque: ")
        CodigoBanco = ingresarGenerico("Ingrese el codigo de Banco: ")
        CodigoSucursal = ingresarGenerico("Ingrese el codigo de la sucursal: ")
        NumeroCuentaOrigen = verificarDNI("Ingrese el numero de cuenta de origen: ")
        NumeroCuentaDestino = verificarDNI("Ingrese el numero de la cuenta de destino: ")
        Valor = verificarValor("Ingrese el valor del cheque: ")
        FechaOrigen = verificarFechas("Ingrese la fecha de origen del cheque: ")
        FechaPago = verificarFechas("Ingrese la fecha de pago del cheque: ")
        dni = verificarDNI("Ingrese su numero de DNI: ")
        Estado = verificarEstado("Ingrese el estado del cheque: ")
        Tipo = verificarTipo("Ingrese el tipo de cheque: ")
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
            strg = verificarDNI("Ingrese el DNI a filtrar: ")
            filtrado(strg,opcion,salida)
        elif(opcion==2):
            strg = verificarTipo("Ingrese el tipo de cheque: ")
            filtrado(strg,opcion,salida)
        elif(opcion==3):
            strg =verificarEstado("Ingrese el estado del cheque: ")
            filtrado(strg,opcion,salida)
        elif(opcion==4):
            strg1 = verificarFechas("Ingrese la primera fecha: ")
            strg2 = verificarFechas("Ingrese la segunda fecha: ")
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
        print("Seleccione una de las opciones para continar")
        print("1-Agregar")
        print("2-Filtrar")
        print("3-Salir")
        opcion = int(input())
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