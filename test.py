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
print(Columnas) #aqui dice que las columnas son 14
print(Conf['ArchivoEntrada'])


#def numColumnas(fila,columnas):
    
Filas = []
contador=0


else:
    print("no pude abrir el archivo {}".format(ArchivoEntrada))"""