from mostrar_datos.carga_datos import carga_dic, export_dic

import numpy as np


def result(cedula, ruta_encuesta):
    encuestados = carga_dic(ruta_encuesta)
    lista_num = encuestados[cedula]['respuestas']
    total = np.sum(lista_num)
    categ = print_categoria(total)
    encuestados['categoria'] = categ
    export_dic(ruta_encuesta, encuestados)



def print_categoria(suma):
    if suma <= 70:
        print('Usted pertenece a la categoria: ARTISTA')
        return 'ARTISTA'
    elif suma <= 92:
        print('Usted pertenece a la categoria: SOCIALES')
        return 'SOCIALES'
    elif suma <= 114:
        print('Usted pertenece a la categoria: INVESTIGADOR')
        return 'INVESTIGADOR'
    elif suma <= 136:
        print('Usted pertenece a la categoria: REALISTA')
        return 'REALISTA'
    elif suma <= 158:
        print('Usted pertenece a la categoria: EMPRENDEDOR')
        return 'EMPRENDEDOR'
    else:
        print('Usted pertenece a la categoria: CONVENCIONAL')
        return 'CONVENCIONAL'
