from mostrar_datos.carga_datos import carga_dic, export_dic

import numpy as np


def result(cedula, ruta_encuesta):
    encuestados = carga_dic(ruta_encuesta)
    lista_num = encuestados[cedula]['respuestas']
    total = np.sum(lista_num)
    categ = print_categoria(total)
    encuestados['categoria'] = categ
    print_compatibilidad(total)
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
def print_compatibilidad(suma):
    a="artes escenicas"
    b="cine y television"
    c="danza" 
    d="arquitectura"
    e="bellas artes"
    f="diseño" 
    g="publicicdad"  
    h="psicologia"
    i="trabjo social"
    j="literatura"
    k="periodismo"    
    l="matematicas"
    m="fisica"
    n="quimica"
    o="medicina"
    p="ingenieria"  
    q="licenciatura"
    r="pedagogia"
    s="derecho"
    t="comunicacion"   
    u="administracion"
    v="economia"
    w="finanzas"
    x="contaduria"  
    y="policia"
    z="ciencias del deporte"
    artista=[a,b,c,d,e,f,g]
    sociales=[h,i,j,k]
    investigador=[l,m,n,o,p]
    realista=[q,r,s,t]
    emprendedor=[u,v,w,x]
    convencional=[y,z]
    l=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
    catalogo=[artista,sociales,investigador,realista,emprendedor,convencional]
    for lo in range(26):
        print(l[lo]) 
    print("escoja tres de las profesiones mostradas y escribala en minusculas ")
    e1=input("ingrese su primera opcion: ")
    while e1 not in l:
        print("corrija su respuesta")
        e1=input("ingrese su primera opcion: ")
    e2=input("ingrese su segunda opcion: ")
    while e2 not in l:
        print("corrija su respuesta")
        e2=input("ingrese su segunda opcion: ")
    e3=input("ingrese su tercera opcion: ")  
    while e3 not in l:
        print("corrija su respuesta")
        e3=input("ingrese su tercera opcion: ")
    if suma <= 70:
        a=catalogo[0]
    elif suma <= 92:
        a=catalogo[1]
    elif suma <= 114:
        a=catalogo[2]
    elif suma <= 136:
        a=catalogo[3]
    elif suma <= 158:
        a=catalogo[4]
    else:
        a=catalogo[5]  
    if e1 in a:
        print("la primera opcion es compatible")
    else:
        print("la primera opcion no es compatible")
    if e2 in a:
        print("la segunda opcion es compatible")
    else:
        print("la segunda opcion no es compatible")
    if e3 in a:
        print("la tercera opcion es compatible")
    else:
        print("la tercera opcion no es compatible")
    en=input("para ver las sugerencias presione enter----->")
    enter=""
    if enter==en:
        print("Estas son las profesiones que le sigerimos de acuerdo a sis resultados:")
        for i in range(len(a)):
            print(a[i])
    
