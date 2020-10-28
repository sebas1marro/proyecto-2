from mostrar_datos.carga_datos import carga_dic, export_dic
from validaciones.validar import val_num, val_gen, val_nombre, val_cedula, val_resp


def llenar_datos(ruta_encuesta):
    encuestados = carga_dic(ruta_encuesta)
    datos = dict()
    print('\n\nBienvenido\n\n')
    cedula = val_cedula('\tDigite su cedula:')
    datos['nombre'] = val_nombre('\tIngrese su nombre: ')
    datos['edad'] = val_num('\tIngrese su edad: ')
    datos['genero'] = val_gen('\tIngrese su genero (1: masculino, 0: femenino): ')
    datos['respuestas'] = []
    encuestados[cedula] = datos
    export_dic(ruta_encuesta, encuestados)
    return cedula


def resp_num(respuesta):
    if respuesta == 'a' or respuesta == 'A':
        return 1
    elif respuesta == 'b' or respuesta == 'B':
        return 2
    else:
        return 3


def preguntar(ruta_encuesta, ruta_preguntas, cedula):
    encuestados = carga_dic(ruta_encuesta)
    preguntas = carga_dic(ruta_preguntas)
    print('\n')
    for pregunta in preguntas:
        respuesta = ''
        print(pregunta)
        for respuestas in preguntas[pregunta]:
            print('\t', respuestas)
        print('\nSeleccione A, B o C')
        respuesta = val_resp('----> ')
        respuesta = resp_num(respuesta)
        encuestados[cedula]['respuestas'].append(respuesta)
    export_dic(ruta_encuesta, encuestados)
