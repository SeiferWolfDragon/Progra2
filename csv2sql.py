import csv
import json
from pathlib import Path
Conf=None
with open("configuracion.json") as jsonfile:
    Conf=json.load(jsonfile)

ArchivoEntrada=Conf['ArchivoEntrada']
ArchivoSalida=Conf['ArchivoSalida']
Tabla=Conf['Tabla']
Columnas=Conf["Columnas"]

def numColumnas(fila,columnas):
    

print(f"abriendo archivo: {ArchivoEntrada}...")
RutaArchivoEntrada = Path(ArchivoEntrada)
if RutaArchivoEntrada.exists():
    with RutaArchivoEntrada.open() as archivocsv:
        print("Se ha Encontrado el archivo")
        lectorCSV=csv.reader(archivocsv,delimiter=',')
        for fila in lectorCSV:
            SQL = f"INSERT INTO {Tabla} VALUES ("
else:
    print("no pude abrir el archivo {}".format(ArchivoEntrada))