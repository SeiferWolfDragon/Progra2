import csv
import json
#import SQL
from pathlib import Path
Conf=None
with open("configuracion_prueba.json") as jsonfile:
    Conf=json.load(jsonfile)
ArchivoEntrada=Conf['ArchivoEntrada']#lleva corchete porqu estamos en diccionario
ArchivoSalida=Conf['ArchivoSalida']
Tabla=Conf['Tabla']
Columnas=Conf["Columnas"]

#def numColumnas(fila,columnas):
    



print(f"abriendo archivo: {ArchivoEntrada}...")
RutaArchivoEntrada = Path(ArchivoEntrada)
if RutaArchivoEntrada.exists():
    with RutaArchivoEntrada.open() as archivocsv:
        print("Se ha Encontrado el archivo")
        lectorCSV=csv.reader(archivocsv,delimiter=',')
        for fila in lectorCSV:
            Columnas.append(fila)
            print(Columnas)
else:
    print("no pude abrir el archivo {}".format(ArchivoEntrada))