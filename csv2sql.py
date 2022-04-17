import csv
import json
<<<<<<< HEAD
#import time
=======
import io
import time
import sqlite3

>>>>>>> 06e92b10473e7d772f5becafd90e99cec7588420
from pathlib import Path

Conf=None
with open("configuracion.json") as jsonfile:
    Conf=json.load(jsonfile)
ArchivoEntrada=Conf['ArchivoEntrada']#lleva corchete porqu estamos en diccionario
ArchivoSalida=Conf['ArchivoSalida']
Tabla=Conf['Tabla']
Columnas=Conf["Columnas"]




#<<<<<<< HEAD


print(f"abriendo archivo: {ArchivoEntrada}...")
#=======
#############Definir cuales son las columnas a usar
def numColumna():
    contadorcol=0
    for c in Columnas:
        contadorcol+=1
        #print(c["posicion"],c["tipo"])
    #print(contadorcol)
    return contadorcol
    #return  #(c["posicion"])

def numFilas():
    contadorlinea = 0
    RutaArchivoEntrada = Path(ArchivoEntrada)
    with RutaArchivoEntrada.open() as archivocsv:
        lectorCSV = csv.reader(archivocsv, delimiter=',')
        archivocsv.readline()
        for fila in lectorCSV:
            contadorlinea += 1
    #print(contadorlinea)
    return contadorlinea
    #return contador

############definir la cantidad de inserts a usar (deben ser 19)

def dictArray():
    for c in Columnas:
        Lista.append([c["posicion"], c["tipo"]])
        #print(c)

def crearFilas():

    RutaArchivoEntrada = Path(ArchivoEntrada)
    with RutaArchivoEntrada.open() as archivocsv:
        archivocsv.readline()
        LectorCSV = csv.reader(archivocsv, delimiter=',')
        for fila in LectorCSV:
            Filas.append(fila)
"""  for i in range(0,len(Filas),1):
            for j in range(0,len(Lista),1):
                dato=Lista[j][0]
                print(Filas[i][dato], end=" ")
                time.sleep(0.5)"""


def convCadaInt(Cad):
    if Cad == '':
        Cad = '0'
    return int(Cad)

    
def imprimir(a,b):
    dato = Lista[b][0]
    if (Lista[b][1] == "Entero"):
       # print(convCadaInt(Filas[i][dato].replace(",", "").replace("22 ", "")), end=" ")
        return convCadaInt(Filas[a][dato].replace(",", "").replace("22 ", ""))
    else:
       #print('"' + str(Filas[i][dato].replace(",", "")) + '"', end=" ")
        return '"' + str(Filas[a][dato].replace(",", "")) + '"'


#print(Columnas)
####COMO CREAR COLUMNAS EN PYTHON PARA CSV "BUSCAR INFORMACION"


Lista=[]
Filas = []
dictArray()
matriz=[Filas,Lista]
crearFilas()
<<<<<<< HEAD
Colun1={}
Colun2=[]
with open('Salida.SQL','w',newline="") as file:
    for i in range(0, len(Filas)):
        for j in range(0, len(Lista)):
            filewriter = csv.writer(file)
            #print(imprimir(i,j))
            filewriter.writerows(str(imprimir(i,j)))
       
=======
cadenita="INSERT INTO "+Tabla+" VALUES ("
destinocsv = open(ArchivoSalida, 'w', newline="")
escritordictCSV = csv.writer(destinocsv)
for i in range(0, len(Filas), 1):
    cadenita = "INSERT INTO " + Tabla + " VALUES ("
    for j in range(0, len(Lista), 1):
        if j==(len(Lista)-1):
           #print(imprimir(i,j), end=' ')
            cadenita=cadenita+str(imprimir(i,j))+");"
        else:
            cadenita=cadenita+str(imprimir(i,j))+","
    escritordictCSV.writerow(cadenita)
    print(cadenita)


"""def EscrituraArchivo(destino):####problema
    destinocsv = open(ArchivoSalida, 'w', newline="")
    escritordictCSV = csv.DictWriter(destinocsv)
    escritordictCSV.writerow(cadenita)
    escritordictSQL = sql.DictWriter(destinocsv, fieldnames=["columnas"], delimiter="|")
    print(columnas)
    escritordictSQL.writerow({"columnas": imprimir(i,j)})
    

destinocsv = open(ArchivoSalida, 'w', newline="")
EscrituraArchivo(destinocsv)"""
>>>>>>> 06e92b10473e7d772f5becafd90e99cec7588420
