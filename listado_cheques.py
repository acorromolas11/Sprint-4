import csv
import datetime
import sys

#-----Extras------

#Función que imprime por pantalla los titulos(keys) de cada cheque
def mostrarTitulo():
    print(f"| NroCheque | CodigoBanco | CodigoSucursal | NumeroCuentaOrigen | NumeroCuentaDestino |Valor |FechaOrigen | FechaPago | DNI | Estado | Tipo |")

#Función que recibe un diccionario y devuelve los valores de cada key(llave)
def mostrarDatos(dict):
    print(f"| {dict['NroCheque']} | {dict['CodigoBanco']} | {dict['CodigoSucursal']} | {dict['NumeroCuentaOrigen']} | {dict['NumeroCuentaDestino']} | {dict['Valor']} | {dict['FechaOrigen']} | {dict['FechaPago']} | {dict['DNI']} | {dict['Estado']} | {dict['Tipo']} |")


#función crearArchivo que recibe por parámetros el archivo csv, el dni ingresado, el filtro y la fecha, todos recibidos como
#string, salvo el filtro que puede ser recibido como una lista de dos strings en el caso de ser una fecha y la fecha que
# es un booleano que determina si el filtro es una fecha o no,
#Luego, abro el archivo en modo lectura y creo uno en modo escritura. Recorro el que abrí en modo escritura y 
# en el caso de que el el archivo que recorro coincida con el dni, el filtro y el tipo escribo el archivo, si coinciden el dni
# el tipo y la fecha se encuentra entre el rango a buscar, escribo el archivo, finalmente, si el DNI y
# el tipo coinciden y el filtro es "00", esto quiere decir que no se ingreso ningún filtro, por lo que
# escibirá el archivo cuando el dni y el tipo coincidan unicamente.    
def crearArchivo(archivo_csv,dni,tipo,filtro,fecha):
    escribio = False
    with open (f"{dni}_{datetime.datetime.now().strftime('%Y-%m-%d')}_.csv","w",newline='') as wfile:
        with open(archivo_csv,"r") as rfile:
            writer = csv.writer(wfile)
            reader = csv.DictReader(rfile)
            writer.writerow(reader.fieldnames)
            for row in reader:
                Dni = row['DNI']
                if(row['Estado']==filtro and row['Tipo']==tipo and dni==Dni):
                    writer.writerow(row.values())
                    escribio = True
                elif(filtro[0]<=row['FechaPago']<=filtro[1] and row['Tipo']==tipo and dni==Dni and fecha):
                    writer.writerow(row.values())
                    escribio = True
                elif(filtro=="00" and row['Tipo']==tipo and dni==Dni):
                    writer.writerow(row.values())
                    escribio = True
        if (not escribio):
            wfile.write("No se econtraron datos")

#Función que verifica que no se encuentren archivos duplicados en el archivo CSV recibido por parametro
#crea una lista de cheques y una lista de "repetidos" la cual almacenará los nros de cheques repetidos.
#Primero se abre el archivo en modo lectura y se lo recorre y por cada Nro de Cheque, se impone una condición,
#si el Nro de cheques ya está en cheques, se lo agrega a la lista de repetidos, finalmente, si "repetidos" 
#es una lista vacía la función retorna False, de lo contrario retorna la lista con los nros de cheques repetidos para
#que el usuario pueda eliminarlos en el csv.

def duplicados(archivo_csv):
    cheques = []
    repetidos = []
    with open (archivo_csv,"r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if(row['NroCheque'] in cheques):
                repetidos.append(row['NroCheque'])
            cheques.append(row['NroCheque'])
    if(repetidos == []):
        return False
    else:
        print(f"Hay cheques duplicados en la cuenta, el/los Nros de cheques repetidos son: {repetidos}")
        return True


#-----Fin Extras------

#----Inicio Filtrado--------

#Función que recibe por parametros el archivo csv, el dni, la salida, el tipo, un filtro y la fecha,
#el archivo,dni,salida y tipo son strings, la fecha es un booleano que determina si el filtro es una fecha
#el filtro es una string y si es una fecha es una lista con dos strings que contienen los rangos de las fechas en las
#cuales se filtrarán los datos.
#El procedimiento es similar al de crearArchivo, solo que en vez de esribir un archivo,
#se imprime en la consola cuando los datos coinciden con los filtros establecidos, además se tiene en cuenta la
#variable salida que en el caso de ser PANTALLA imprime los datos por pantalla y en el caso de ser CSV llama a la
#función crearArchivo

def filtrado(archivo_csv,dni,salida,tipo,filtro,fecha):
    mostro = False
    if(duplicados(archivo_csv)):
        return
    if(salida == "pantalla"):
        with open(archivo_csv,"r") as file:
            reader = csv.DictReader(file)
            if(salida == "pantalla"):
                mostrarTitulo()
                for row in reader:
                    Dni = row['DNI']
                    if(row["Estado"]==filtro and row['Tipo']==tipo and Dni==dni):
                        mostrarDatos(row)
                        mostro = True
                    elif(filtro[0]<=row["FechaPago"]<=filtro[1] and row['Tipo']==tipo and Dni==dni and fecha):
                        mostrarDatos(row)
                        mostro = True
                    elif(filtro=="00" and row['Tipo'] and Dni==dni):
                        mostrarDatos(row)
                        mostro = True
        if(not mostro):
            print("No se Encontraron datos!")
    elif(salida == "csv"):
        crearArchivo(archivo_csv,dni,tipo,filtro,fecha)
    

#----Fin Filtrado--------             


#----MAIN------
#La parte principal del programa, toma los argumentos de la linea de comando y las almacena en las varibales:
# archivo_py, archivo_csv, dni, salida, tipo, variable y luego declara 3 variables booleanas
#valido, fecha y seguir, la primera verifica que los datos ingresados sean validos, el segundo
#indica si el filtro es un rango de fechas o es un estado del cheque, el último indica si se debe continuar o no.
#En el caso de tener mas de 5 argumentos de linea de comando se le da un valor a la variable, de tener 5 o menos, la varibale
#queda en "00" lo que significa que no se filtrará según otro parametro que no sea dni o tipo de cheque.
#finalmente hay ifs que validan que el ingreso de argumentos por linea de comando sea valido.

#El ingreso debe ser de la siguiente manera:
# python listado_cheques.py cheques.csv(nombre del archivo csv) DNI SALIDA(PANTALLA O CSV) TIPO(EMITIDO O DEPOSITADO)
# VARIABLE(APROBADO, RECHAZADO, PENDIENTE o --fecha si es una fecha) FECHA(--fecha YYYY/MM/DD:YYYY/MM/DD)

archivo_py = sys.argv[0]
archivo_csv = sys.argv[1]
dni = sys.argv[2]
salida = sys.argv[3]
tipo = sys.argv[4]
variable = "00"

valido = True
fecha = False
seguir = True

salida = salida.lower()
tipo = tipo.lower()

if(len(sys.argv)>5):
    variable = sys.argv[5]
    variable = variable.lower()
    
    if(variable.__contains__("-")):
        fecha = True
        variable = sys.argv[6]
        variable = variable.split(":")
        if(variable[0]>variable[1]):
            seguir=False
            print("La primera fecha no puede ser mayor a la segunda!")
        if(seguir):
            for fecha in variable:
                for letra in fecha:
                    if(not("0"<=letra<="9") and letra!="-"):
                        valido = False
                mini_fecha = fecha.split("-")
                if(len(mini_fecha[0])!=4 or len(mini_fecha[1])!=2 or len(mini_fecha[2])!=2 or not valido):
                    seguir = False
                    print("Error en el rango de fechas, el rango de fechas es: YYYY/MM/DD:YYYY/MM/DD")
                    break   

    if(variable!="pendiente" and variable!="aprobado" and variable!="rechazado" and not fecha):
        seguir = False
        print("Error en la variable, la misma debe ser, 'pendiente','aprobado', 'rechazado' o un rango de fechas(YYYY/MM/DD:YYYY/MM/DD)")



if(salida!="pantalla" and salida!="csv"):
    seguir = False
    print("Error en la salida, la salida es: 'PANTALLA' o 'CSV'")

if(tipo!="emitido" and tipo!="depositado"):
    seguir = False
    print("Error en el tipo de cheque, el tipo de cheque es: 'EMITIDO' o 'DEPOSITADO'")



if(seguir):
    filtrado(archivo_csv,dni,salida,tipo,variable,fecha)
#----FIN MAIN-----