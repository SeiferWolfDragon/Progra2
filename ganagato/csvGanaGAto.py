import csv
import json
from pathlib import Path
from datetime import datetime
import pymysql.cursors

with open("accesoJson.json") as jsonfile:
    Conf = json.load(jsonfile)
RutaCSV = Path(Conf['ArchivoEntrada'])
if RutaCSV.exists():
    Datos = []
    with RutaCSV.open() as ArchivoCSV:
        ArchivoCSV.readline()
        Lector = csv.reader(ArchivoCSV)
        for fila in Lector:
            # print(fila)
            Datos.insert(0, fila)
    ###############################################
    connection = pymysql.connect(
        host=Conf['HOST'], user=Conf['DBUSER'],
        password=Conf['DBPASS'], database=Conf['DBNAME'],
        charset='utf8mb4', port=Conf['PORT']
    )
    if connection:
        print("Se pudo establecer la conexion")
        MiCursor = connection.cursor()
        SQL = "insert into ganagato values (20,null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for fila in Datos:
            D = []
            D.append(int(fila[2]))
            D.append(int(fila[3]))
            D.append(int(fila[4]))
            D.append(int(fila[5]))
            D.append(int(fila[6]))
            D.append(int(fila[7]))
            D.append(int(fila[8]))
            D.append(int(fila[9]))
            D.append(int(fila[10]))
            D.append(datetime.strptime(fila[11], '%d/%m/%Y'))
            print(D)
            MiCursor.execute(SQL, D)

        connection.commit()
