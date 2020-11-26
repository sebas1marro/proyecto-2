#   Funciones que validan la respuesta ingresada, si es incorrecta devuelve error hasta que 
#   se cumpla
def val_num(mensaje):
    numero = input(mensaje)
    while not numero.isnumeric():
        print('Debe ser un numero entero')
        numero = input(mensaje)
    return str(numero)

#valida el genero ingresado
def val_gen(mensaje):
    numero = input(mensaje)
    while numero != '0' and numero != '1':
        print('\nDebe ser 1 para masculino 0 para femenino\n')
        numero = input(mensaje)
    return int(numero)

#valida el nombre
def val_nombre(mensaje):
    nombre = input(mensaje)
    while nombre.isnumeric():
        print('\nDigite bien su nombre por favor\n')
        nombre = input(mensaje)
    return nombre

#valida l identificacion 
def val_cedula(mensaje):
    cedula = input(mensaje)
    while not cedula.isnumeric():
        print('\nDebe ser un numero entero\n')
        cedula = input(mensaje)
    return cedula

#distingue si debe continuar o parar
def val_opcion(mensaje):
    opci = input(mensaje)
    while opci != '' and opci != '0' and opci!= '1':
        print('\nIngrese una opcion correcta\n')
        opci = input(mensaje)
    return opci

#   El programa distingue entre minúsculas y mayúsculas.
def val_resp(mensaje):
    resp = input(mensaje)
    respuestas = ['a', 'b', 'c', 'A', 'B', 'C']
    while resp not in respuestas:
        print('\nSeleccione bien su respuesta')
        resp = input(mensaje)
    return resp
