from procedimientos.preguntas import preguntar, llenar_datos
from procedimientos.resultados import result
from validaciones.validar import val_opcion
import pandas as pd
#se necesita instalar tabulate, pegue el siguiente link es u terminal: conda install -c conda-forge tabulate

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
    print("\n Se necesita instalar tabulate: conda install -c conda-forge tabulate")
    print('\n\n\t\tTest Vocacional\n\n')
    opcion = val_opcion('Presione enter para empezar con la encuesta 0 de lo contrario --->')
    while opcion != '0':
        while opcion == '':
            cedula = llenar_datos(ruta)
            preguntar(ruta, ruta_preguntas, cedula)
            result(cedula, ruta)
            opcion = val_opcion('Presione enter para empezar con la encuesta, 1 para ver los datos guardados y 0 para salir --->')
        if opcion =='1':
            datos=pd.read_csv("datos voc.csv", names=['cedula','nombre','edad','genero','categoria','elec_1','elec_2','elec_3','comp_1','comp_2','comp_3','comp_4','comp_5','comp_6','comp_7'])
            print(datos)
            opcion = val_opcion('Presione enter para empezar con la encuesta, 1 para ver los datos guardados y 0 para salir --->')
    print('Hasta luego')    

main()


