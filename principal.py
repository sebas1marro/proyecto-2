from procedimientos.preguntas import preguntar, llenar_datos
from procedimientos.resultados import result
from validaciones.validar import val_opcion

#   El programa empieza pidiendole al usuario datos personales tales como:
#   nombre. cedula. edad. genero (1 masculino, 0 femenino) 
#   Del módulo preguntas, la ruta almacenará los datos ingresados en la primera parte
#   y del archivo de las preguntas tomará cada pregunta con sus respectivas respuestas(ver preguntas) 
def main():
    """
    Función principal
    """
    ruta = "./datos/datos.json"
    ruta_preguntas = "./datos/respuestas.json"
    print('\n\n\t\tTest Vocacional\n\n')
    opcion = val_opcion('Presione enter para empezar con la encuesta 0 de lo contrario --->')
    while opcion == '':
        cedula = llenar_datos(ruta)
        preguntar(ruta, ruta_preguntas, cedula)
        result(cedula, ruta)
        opcion = val_opcion('Presione enter para empezar con la encuesta 0 de lo contrario --->')
    print('Hasta luego')


main()



