# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 17:09:58 2022

@author: diego
"""

import csv
import json
#import SQL
from pathlib import Path
Conf=None
with open("configuracion.json") as jsonfile:
    Conf=json.load(jsonfile)

ArchivoEntrada=Conf['ArchivoEntrada']#lleva corchete porqu estamos en diccionario
ArchivoSalida=Conf['ArchivoSalida']
Tabla=Conf['Tabla']
Columnas=Conf["Columnas"]
print(len(Columnas)) #aqui dice que las columnas son 14


#def numColumnas(fila,columnas):
    
Filas = []
contador=0

"""def convCadaInt(Cad):
     if Cad == '':
          Cad = '0'
     return int(Cad)

print(f"abriendo archivo: {ArchivoEntrada}...")
RutaArchivoEntrada = Path(ArchivoEntrada)
if RutaArchivoEntrada.exists():
    with RutaArchivoEntrada.open() as archivocsv:
        archivocsv.readline()
        print("Se ha Encontrado el archivo")
        lectorCSV=csv.reader(archivocsv,delimiter=',')
        for fila in lectorCSV:
            print(fila)
            Filas.append(fila)
            contador += 1
        Cad_Forma='INSERT INTO Municipios VALUES ({},"{}",{},{},{},{},{},{},{},{},{},{},{},{})'
       # print(Cad_Forma)
        for n in range(0, contador, 1):
            print(Cad_Forma.format(Filas[n][0].replace("22 ",""),
                  Filas[n][1],
                  convCadaInt(Filas[n][3].replace(",","")),
                  convCadaInt(Filas[n][4].replace(",","")),
                  convCadaInt(Filas[n][5].replace(",","")),
                  convCadaInt(Filas[n][6].replace(",","")),
                  convCadaInt(Filas[n][7].replace(",","")),
                  convCadaInt(Filas[n][8].replace(",","")),
                  convCadaInt(Filas[n][9].replace(",","")),
                  convCadaInt(Filas[n][10].replace(",","")),
                  convCadaInt(Filas[n][11].replace(",","")),
                  convCadaInt(Filas[n][12].replace(",","")),
                  convCadaInt(Filas[n][13].replace(",","")),
                  convCadaInt(Filas[n][14].replace(",",""))))
else:
    print("no pude abrir el archivo {}".format(ArchivoEntrada))"""