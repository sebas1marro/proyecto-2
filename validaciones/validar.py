def val_num(mensaje):
    numero = input(mensaje)
    while not numero.isnumeric():
        print('Debe ser un numero entero')
        numero = input(mensaje)
    return int(numero)


def val_gen(mensaje):
    numero = input(mensaje)
    while numero != '0' and numero != '1':
        print('\nDebe ser 1 para masculino 0 para femenino\n')
        numero = input(mensaje)
    return int(numero)


def val_nombre(mensaje):
    nombre = input(mensaje)
    while nombre.isnumeric():
        print('\nDigite bien su nombre por favor\n')
        nombre = input(mensaje)
    return nombre


def val_cedula(mensaje):
    cedula = input(mensaje)
    while not cedula.isnumeric():
        print('\nDebe ser un numero entero\n')
        cedula = input(mensaje)
    return cedula


def val_opcion(mensaje):
    opci = input(mensaje)
    while opci != '' and opci != '0':
        print('\nIngrese una opcion correcta\n')
        opci = input(mensaje)
    return opci


def val_resp(mensaje):
    resp = input(mensaje)
    respuestas = ['a', 'b', 'c', 'A', 'B', 'C']
    while resp not in respuestas:
        print('\nSeleccione bien su respuesta')
        resp = input(mensaje)
    return resp
