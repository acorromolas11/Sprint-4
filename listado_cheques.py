import csv
import datetime
import sys

#-----Extras------

#Función que imprime por pantalla los titulos(keys) de cada cheque
def mostrarTitulo():
    print(f"|NroCheque|CodigoBanco|CodigoSucursal|NumeroCuentaOrigen|NumeroCuentaDestino|Valor|FechaOrigen|FechaPago|DNI|Estado|Tipo|")

#Función que recibe un diccionario y devuelve los valores de cada key(llave)
def mostrarDatos(dict):
    print(f"|{dict['NroCheque']}|{dict['CodigoBanco']}|{dict['CodigoSucursal']}|{dict['NumeroCuentaOrigen']}|{dict['NumeroCuentaDestino']}|{dict['Valor']}|{dict['FechaOrigen']}|{dict['FechaPago']}|{dict['DNI']}|{dict['Estado']}|{dict['Tipo']}|")

#Función que recibe por parametro un archivo csv, el dni ingresado, el valor filtro (string que contiene el valor que se
#desea filtrar, ya sea Pendiente,Aprobado,Rechazado) y un rango de fechas que es una lista que contiene dos fechas que
#determinan de que fecha a que fecha se filtrarán los datos.

#La función recorre el archivo recibido por parametro mediante una apertura del mismo en modo lectura y crea un nuevo
#archivo con el nombre del dni que se usa como filtro y si el DNI, el ESTADO del cheque y el TIPO de cheque coinciden
#Escribe en el nuevo archivo. La operación es la misma para las fechas solo que verifica que en el archivo que 
#se está leyendo la fecha se encuentre en el rango.

def crearArchivo(archivo_csv,dni,filtro,fecha):
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
                elif(filtro[0]<row['FechaPago']<filtro[1] and row['Tipo']==tipo and dni==Dni and fecha):
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
#Función que recibe por parametro el archivo CSV, el DNI, el tipo de salida(string que contiene "PANTALLA" o "CSV")
#tipo que es una string que especifica el tipo de cheque, filtro que es una string que especifica el estado, y fecha,
# un lista que contiene las dos fechas que establecen el rango de fechas
# La Función filtrado recorre la variabl archivo_csv abriendolo en modo lectura y compara que
# el dni, el tipo y el filtro ingresados coincidan, en caso de hacerlo, si la salida es "PANTALLA", los muestra por pantalla
# si la salida es "CSV" crea un archivo CSV con los datos que coinciden. 
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
                    elif(filtro[0]<row["FechaPago"]<filtro[1] and row['Tipo']==tipo and Dni==dni and fecha):
                        mostrarDatos(row)
                        mostro = True
        if(not mostro):
            print("No se Encontraron datos!")
    elif(salida == "csv"):
        crearArchivo(archivo_csv,dni,filtro,fecha)
    

#----Fin Filtrado--------             


#----MAIN------
#El primer print establece como deben escribirse los datos para utilizar el programa
#Se declaran las varibales archivo_py,archivo_csv,dni,salida,tipo y variable
#Las mismas contienen los datos ingresados como argumentos en la linea de comando.

#Luego se declaran las variables valido,fecha y seguir que son banderas, las cuales establecen si,
#el valor ingresado como argumento de linea de comando es valido, si la variable a filtrar es una fecha y
#si el programa debe continuar su ejecución

#Luego, las strings que se compararán con otras strings se pasan a lower para que no hayan errores de mayúsculas


print("Uso python listado_cheques.py cheques.csv DNI SALIDA TIPO VARIABLE FECHA")

archivo_py = sys.argv[0]
archivo_csv = sys.argv[1]
dni = sys.argv[2]
salida = sys.argv[3]
tipo = sys.argv[4]
variable = sys.argv[5]

valido = True
fecha = False
seguir = True

salida = salida.lower()
variable = variable.lower()
tipo = tipo.lower()

if(salida!="pantalla" and salida!="csv"):
    seguir = False
    print("Error en la salida, la salida es: 'PANTALLA' o 'CSV'")

if(tipo!="emitido" and tipo!="depositado"):
    seguir = False
    print("Error en el tipo de cheque, el tipo de cheque es: 'EMITIDO' o 'DEPOSITADO'")


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
    print("Error en la salida, la salida es: 'PANTALLA' o 'CSV'")

if(seguir):
    filtrado(archivo_csv,dni,salida,tipo,variable,fecha)
#----FIN MAIN-----