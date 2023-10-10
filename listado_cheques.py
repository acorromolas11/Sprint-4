import csv
import datetime
import sys

#-----Extras------

def mostrarTitulo():
    print(f"|NroCheque|CodigoBanco|CodigoSucursal|NumeroCuentaOrigen|NumeroCuentaDestino|Valor|FechaOrigen|FechaPago|DNI|Estado|Tipo|")

def mostrarDatos(dict):
    print(f"|{dict['NroCheque']}|{dict['CodigoBanco']}|{dict['CodigoSucursal']}|{dict['NumeroCuentaOrigen']}|{dict['NumeroCuentaDestino']}|{dict['Valor']}|{dict['FechaOrigen']}|{dict['FechaPago']}|{dict['DNI']}|{dict['Estado']}|{dict['Tipo']}|")

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