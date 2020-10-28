import json


def carga_dic(ruta: str):
    archivo = open(ruta, "r")
    datos = json.loads(archivo.read())
    archivo.close()
    return datos

def export_dic(ruta, encuestados):
    archivo = open(ruta, 'w')
    dicciona = json.dumps(encuestados, indent=3)
    archivo.write(dicciona)
    archivo.close()
