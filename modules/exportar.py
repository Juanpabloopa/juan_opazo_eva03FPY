import csv
import json


def exportar(rutaj,rutac):
    if not rutaj.exists() and rutaj.stat().st_size==0:
        print('El archivo no existe o esta vacio')
    else:
        with open(rutac,mode='w') as cffiles:


            json_file= csv.writer(cffiles)
