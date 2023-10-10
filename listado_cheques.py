import csv
from collections import defaultdict
import datetime
import sys

#-----Extras------

def mostrarTitulo():
    print(f"|NroCheque|CodigoBanco|CodigoSucursal|NumeroCuentaOrigen|NumeroCuentaDestino|Valor|FechaOrigen|FechaPago|DNI|Estado|Tipo|")

def mostrarDatos(dict):
    print(f"|{dict['NroCheque']}|{dict['CodigoBanco']}|{dict['CodigoSucursal']}|{dict['NumeroCuentaOrigen']}|{dict['NumeroCuentaDestino']}|{dict['Valor']}|{dict['FechaOrigen']}|{dict['FechaPago']}|{dict['DNI']}|{dict['Estado']}|{dict['Tipo']}|")

def crearArchivo(dni,filtro,fecha):
    escribio = False
    with open (f"{dni}_{datetime.datetime.now().strftime('%Y-%m-%d')}_.csv","w",newline='') as wfile:
        with open("cheques.csv","r") as rfile:
            writer = csv.writer(wfile)
            reader = csv.DictReader(rfile)
            writer.writerow(reader.fieldnames)
            for row in reader:
                Dni = row['DNI']
                Dni = int(Dni)
                if(row['Tipo']==filtro and dni==Dni):
                    writer.writerow(row.values())
                    escribio = True
                elif(row['Estado']==filtro and dni==Dni):
                    writer.writerow(row.values())
                    escribio = True
                elif(row['FechaOrigen'] and dni==Dni and fecha):
                    writer.writerow(row.values())
                    escribio = True
        if (not escribio):
            wfile.write("No se econtraron datos")

#-----Fin Extras------

#----Inicio Filtrado--------
def filtrado(dni,filtro,salida,archivo_csv,fecha):
    mostro = False
    if(salida == "pantalla"):
        with open(archivo_csv,"r") as file:
            reader = csv.DictReader(file)
            if(salida == "pantalla"):
                mostrarTitulo()
                for row in reader:
                    Dni = row["DNI"]
                    Dni = int(Dni)
                    if(row["Tipo"]==filtro and Dni==dni):
                        mostrarDatos(row)
                        mostro = True
                    elif(row["Estado"]==filtro and Dni==dni):
                        mostrarDatos(row)
                        mostro = True
                    elif(row["FechaOrigen"]<filtro and Dni==dni and fecha):
                        mostrarDatos(row)
                        mostro = True
        if(not mostro):
            print("No se Encontraron datos!")
    elif(salida == "csv"):
        crearArchivo(dni,filtro,fecha)
    

#----Fin Filtrado--------             

#----MAIN------
if (len(sys.argv)!= 7):
    print("Uso python listado_cheques.py cheques.csv DNI SALIDA VARIABLE")
print(sys.argv[0],sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
archivo_py = sys.argv[0]
archivo_csv = sys.argv[1]
dni = sys.argv[2]
salida = sys.argv[3]
variable = sys.argv[4]
dni = int(dni)
salida = salida.lower()
variable = variable.lower()

fecha = False
if(variable.__contains__("-")):
    fecha = True

filtrado(dni,variable,salida,archivo_csv,fecha)
#----FIN MAIN-----