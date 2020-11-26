from mostrar_datos.carga_datos import carga_dic, export_dic
#se necesita instalar tabulate, si no lo tiene pegue el siguiente link en la terminal: conda install -c conda-forge tabulate
print("se necesita instalar tabulate, si no lo tiene pegue el siguiente link en la terminal: conda install -c conda-forge tabulate")
from tabulate import tabulate
import numpy as np

#procesa los datos con otroas funciones y da la informacion de respuesta
def result(cedula, ruta_encuesta):
    encuestados = carga_dic(ruta_encuesta)
    lista_num = encuestados[cedula]['respuestas']
    total = np.sum(lista_num)
    tabla={'PUNTAJE':['0-70',
                      '71-92',
                      '93-114',
                      '115-136',
                      '137-158',
                      '159-180'],
           'CATEGORIA':['ARTISTA',
                        'SOCIALES',
                        'INVESTIGADOR',
                        'REALISTA',
                        'EMPRENDEDOR',
                        'CONVENCIONAL']}
    print(tabulate(tabla, headers=['PUNTAJE','categoria']))    
    categ = print_categoria(total)
    encuestados['categoria'] = categ
    print_compatibilidad(total)
    export_dic(ruta_encuesta, encuestados)


#recibe las opciones y da respuesta y sugerencias segun categoria a la que pertenece
def print_categoria(suma):
    if suma <= 70:
        print('Usted pertenece a la categoria: ARTISTA')
        c= 'ARTISTA'
        cat=open("voc.csv","a")
        cat.write(c +'\n')
        cat.close()
        return c
 
    elif suma <= 92:
        print('Usted pertenece a la categoria: SOCIALES')
        c='SOCIALES'
        cat=open("voc.csv","a")
        cat.write(c +'\n')
        cat.close()
        return c
    elif suma <= 114:
        print('Usted pertenece a la categoria: INVESTIGADOR')
        c= 'INVESTIGADOR'
        cat=open("voc.csv","a")
        cat.write(c +'\n')
        cat.close()
        return c  
    elif suma <= 136:
        print('Usted pertenece a la categoria: REALISTA')
        c= 'REALISTA'
        cat=open("voc.csv","a")
        cat.write(c +'\n')
        cat.close()
        return c
    elif suma <= 158:
        print('Usted pertenece a la categoria: EMPRENDEDOR')
        c= 'EMPRENDEDOR'
        cat=open("voc.csv","a")
        cat.write(c +'\n')
        cat.close()
        return c   
    else:
        print('Usted pertenece a la categoria: CONVENCIONAL')
        c= 'CONVENCIONAL'
        cat=open("voc.csv","a")
        cat.write(c +'\n')
        cat.close()
        return c

def print_compatibilidad(suma):
    a="artes escenicas"
    b="cine y television"
    c="danza" 
    d="arquitectura"
    e="bellas artes"
    f="diseño" 
    g="publicicdad"  
    h="psicologia"
    i="trabajo_social"
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
    #seleccion y compatibilidad
    print("escoja tres de las profesiones mostradas y escribala en minusculas ")

    e1=input("ingrese su primera opcion: ")
    while e1 not in l:
        print("corrija su respuesta")
        for lo in range(26):
            print(l[lo]) 
        e1=input("ingrese su primera opcion: ")
    for lo in range(26):
        print(l[lo]) 
    e2=input("ingrese su segunda opcion: ")
    while e2 not in l:
        print("corrija su respuesta")
        for lo in range(26):
            print(l[lo]) 
        e2=input("ingrese su segunda opcion: ")
    for lo in range(26):
        print(l[lo]) 
    e3=input("ingrese su tercera opcion: ")  
    while e3 not in l:
        print("corrija su respuesta")
        for lo in range(26):
                print(l[lo]) 
        e3=input("ingrese su tercera opcion: ")
    prof=open("seleccion prof.csv","a")
    prof.write(e1)
    prof.write(",")
    prof.write(e2)
    prof.write(",")  
    prof.write(e3)
    prof.write("\n")        
    prof.close()
    
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
    #sugerencias compatibles
    en=input("para ver las sugerencias presione enter----->")
    enter=""
    if enter==en:
        print("Estas son las profesiones que le sugerimos de acuerdo a sus resultados:")
        for i in range(len(a)-1):
            print(a[i])
            sug=open("compa.csv","a")
            sug.write(a[i])
            sug.write(",")
            sug.close()
        sug=open("compa.csv","a")
        x=len(a)
        sug.write(a[x-1]+'\n')
        sug.close()
