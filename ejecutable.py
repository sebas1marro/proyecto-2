# -*- coding: utf-8 -*-
from tkinter import *
from mostrar_datos.carga_datos import carga_dic, export_dic
import numpy as np
from tabulate import tabulate
import pandas as pd

#Definición de funciones---------------------------------------------
    #Advertencias. Errores:
def val_num():
    numero = edad.get()
    if not numero.isnumeric():
        messagebox.showerror("Advertencia", "Edad debe ser un número entero!")
    else: return True
          
def val_gen():
    numero = genero.get()
    if numero != '0' and numero != '1':
        messagebox.showerror("Advertencia", '\nDebe ser 1 para masculino 0 para femenino\n')
    else: return True  
def val_nombre():
    nombre = username.get()
    if nombre.isnumeric():
        messagebox.showerror("Advertencia",'\nDigite bien su nombre por favor\n')
    else: return True
def val_cedula():
    documento = cedula.get()
    if not documento.isnumeric():
        messagebox.showerror("Advertencia", "Documento debe ser un número entero!")
    else: return True   
def validacion():
    global identity
    val_num()
    val_gen()
    val_nombre()
    val_cedula()
    ruta = "./datos/datos.json"
    if val_num() and val_gen() and val_nombre() and val_cedula() == True: 
        respuesta = messagebox.askyesno("Correcto", '\n\nBienvenido\n\n El cuestionario consta de 60 preguntas, ¿desea continuar?')
        if respuesta == True:
            identity = llenar_datos(ruta)
            delete()
def val_resp(mensaje):
    resp = input(mensaje)
    respuestas = ['a', 'b', 'c', 'A', 'B', 'C']
    while resp not in respuestas:
        print('\nSeleccione bien su respuesta')
        resp = input(mensaje)
    return resp
    
    #Preguntas:
def llenar_datos(ruta_encuesta):
    encuestados = carga_dic(ruta_encuesta)
    datos = dict()
    documento = cedula.get()
    datos['nombre'] = username.get()
    datos['edad'] = edad.get()
    datos['genero'] = genero.get()
    datos['respuestas'] = []
    encuestados[documento] = datos
    if(datos['genero']==0):
        g="Femenino"
    else:
        g="Masculino"
    info=open("datos voc.csv","a")
    info.write(documento)
    info.write(",")
    info.write(datos['nombre'])
    info.write(",")  
    info.write(datos['edad'])
    info.write(",")  
    info.write(str(g))
    info.write(",")           
    info.close()  
    export_dic(ruta_encuesta, encuestados)
    return documento

def resp_num(respuesta):
    if respuesta == 'a' or respuesta == 'A':
        return 1
    elif respuesta == 'b' or respuesta == 'B':
        return 2
    else:
        return 3

#   Función que calcula el puntaje total y lo guarda.
def result(cedula, ruta_encuesta):
    global total
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
    
    export_dic(ruta_encuesta, encuestados)
 

#Funciones del formulario-------------------------------------------------------------
def delete():
    global global_label
    global global_label2
    global username_label
    global cedula_label
    global edad_label
    global genero_label
    global username_entry
    global cedula_entry
    global edad_entry
    global genero_entry
    global boton_listo
    global boton_atras
    global valorpreguntas
    global contador
    global contador2
    boton_listo.destroy()
    boton_atras.destroy()
    cedula_entry.destroy()
    username_entry.destroy()
    edad_entry.destroy()
    genero_entry.destroy()
    username_label.destroy()
    cedula_label.destroy()
    edad_label.destroy()
    genero_label.destroy()
    global_label.destroy()
    global_label2 = Label(text = "Por favor, responda las siguientes preguntas:", bg = "#213141",  font = ("Times",20, "italic"), fg = "white")
    global_label2.place(x = 50, y = 80)
    boton_salir.place(x = 550, y = 200)
    boton_siguiente.place(x = 300, y = 500)
    valorpreguntas = 0
    generador()
    botonescheck()
    contador = 1
    contador2 = 1

#   Función que genera la lista de las preguntas y las listas apartes para cada opción. En esencia, para A,B y C.    
def botonescheck():
    global boton_A
    global boton_B
    global boton_C
    global preguntas_label
    global var
    global listapreguntas
    global respuesta1
    global respuesta2
    global respuesta3
    encuestados = carga_dic("./datos/datos.json")
    preguntas = carga_dic("./datos/respuestas.json")
    listapreguntas = list()
    listarespuestas = list()
    respuesta1 = list()
    respuesta2 = list()
    respuesta3 = list()
    for pregunta in preguntas:
        respuesta = ''
        listapreguntas.append(pregunta)
        #print(listapreguntas)
        for respuestas in preguntas[pregunta]:
            listarespuestas.append(respuestas)
    for i in range(0, 180,3):
        respuesta1.append(listarespuestas[i]) 
    for i in range(1, 180,3):
        respuesta2.append(listarespuestas[i]) 
    for i in range(2, 180,3):
        respuesta3.append(listarespuestas[i])
    #return respuesta2
    preguntas_label = Label(text = listapreguntas[0],  bg = "#213141",  font = ("Times",10, "italic"), fg = "white") 
    preguntas_label.place(x = 30, y = 150)
    
#   Radiobutton. Guarda el valor seleccionado.
def onclick():
    global var
    global valor    
    valor = var.get()
    
#   función que genera todas las preguntas con sus respectivas respuestas
def delete2():
    global boton_A
    global boton_B
    global boton_C
    global valorpreguntas
    global preguntas_label
    global listapreguntas
    global respuesta1
    global respuesta2
    global respuesta3
    global var
    global contador
    global contador2
    ruta = "./datos/datos.json"
    var.set(0)
    #   Se implementa un valor condicional a la función delete, si es igual a 1, 
    #   pasará a la siguiente pregunta, si no se selecciona ninguna respuesta, no dejará continuar.
    if contador != 60:
        if valorpreguntas == 1:
            preguntas_label.destroy()
            preguntas_label = Label(text = listapreguntas[contador],  bg = "#213141",  font = ("Times",10, "italic"), fg = "white") 
            preguntas_label.place(x = 30, y = 150)
            contador += 1
            valorpreguntas = 0
            boton_A.destroy()
            boton_B.destroy()
            boton_C.destroy()
            boton_A = Radiobutton(mywindow, text=respuesta1[contador2], variable=var, value=1,
                  command=onclick)
            boton_B = Radiobutton(mywindow, text=respuesta2[contador2], variable=var, value=2,
                  command=onclick)
            boton_C = Radiobutton(mywindow, text=respuesta3[contador2], variable=var, value=3,
                  command=onclick)
            generador()
            contador2 += 1
            valorpreguntas = 0
            #break
    else:
        result(identity, ruta) 

#   Generar los primeros botones             
def generador(): 
    boton_A.place(x = 100, y = 250)
    boton_B.place(x = 100, y = 320)
    boton_C.place(x = 100, y = 390)
    
#   Guarda las respuestas en el archivo json    
def checkbox_clicked():
    global var
    global valorpreguntas
    global valor
    global boton_A
    global boton_B
    global boton_C
    ruta = "./datos/datos.json"
    encuestados = carga_dic(ruta)
    opcion = 0
    valorpreguntas = 0
    if valor == 1:
        respuesta = resp_num('A')
        opcion = 1
        encuestados[identity]['respuestas'].append(respuesta)
    if valor == 2:
        respuesta = resp_num('B')
        opcion = 2
        encuestados[identity]['respuestas'].append(respuesta)
    if valor == 3:
        respuesta = resp_num('C')
        opcion = 3
        encuestados[identity]['respuestas'].append(respuesta)
    export_dic(ruta, encuestados)
    if opcion != 0:
        if opcion == 1:
            valorpreguntas = 1
            delete2()
        elif opcion == 2:
            valorpreguntas = 1
            delete2()
        elif opcion == 3:
            valorpreguntas = 1
            delete2()
    else:
        messagebox.showerror("Advertencia", "Por favor, escoja una opcion")

#   Ventana de recomendaciones    
def delete3():
    global otra_ventana
    global otra_ventana2
    otra_ventana.destroy()
    otra_ventana2 = Toplevel()
    otra_ventana2.title('Recomendaciones')
    otra_ventana2.configure(bg = "#213141")
    otra_ventana2.geometry('800x600')
    sugerencias = Label(otra_ventana2, text = "Carreras recomendadas:", bg = "#213141",  font = ("Times",20, "italic"), fg = "white")
    sugerencias.place(x = 150, y = 350)
    boton_sugerencias = Button(otra_ventana2,text = "Mostrar", width = "10", height = "2", command=funsuger , bg = "burlywood", font = ("Times",16, "bold"))
    boton_sugerencias.place(x = 300, y = 430)
    atrventana3(total)
    
#   Funcines de carreras sugeridas por el programa----------------------------------------
def print_compatibilidad():
    global opciones
    global profesiones
    global opciones2
    global boton_opciones2
    global profesiones2
    global e1
    global l
    global boton_opciones
    global catalogo
    mywindow.iconify()
    a="artes escenicas"
    b="cine y television"
    c="danza" 
    d="arquitectura"
    e="bellas artes"
    f="diseño" 
    g="publicidad"  
    h="psicologia"
    i="trabajo social"
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
    e1= opciones.get()
    numero = 0
    if e1 not in l:
        messagebox.showerror("Advertencia", "Corrija su respuesta")
    else:
        messagebox.showerror("Advertencia", "Ingrese su segunda opcion:")
        opciones2 = StringVar()
        boton_opciones.destroy()
        profesiones.destroy()
        boton_opciones2 = Button(otra_ventana,text = "Ok", width = "10", height = "2", command=datose2 , bg = "burlywood", font = ("Times",16, "bold"))
        boton_opciones2.place(x = 180, y = 500)
        profesiones2 = Entry(otra_ventana, textvariable = opciones2, bg = "saddlebrown", width = "30", font=("Helvetica",14,"bold")) 
        profesiones2.place(x=70,y=490)

def datose2():
    global opciones3
    global opciones2
    global profesiones2
    global profesiones3
    global e2
    global boton_opciones2
    global boton_opciones3
    global l
    e2 = opciones2.get()
    if e2 not in l:
        messagebox.showerror("Advertencia", "Corrija su respuesta")
    else:
        messagebox.showerror("Advertencia", "Ingrese su tercera opcion:")
        opciones3 = StringVar()
        profesiones2.destroy()
        boton_opciones2.destroy()
        boton_opciones3 = Button(otra_ventana,text = "Ok", width = "10", height = "2", command=datose3 , bg = "burlywood", font = ("Times",16, "bold"))
        boton_opciones3.place(x = 180, y = 500)
        profesiones3 = Entry(otra_ventana, textvariable = opciones3, bg = "saddlebrown", width = "30", font=("Helvetica",14,"bold")) 
        profesiones3.place(x=70,y=490)

def datose3():
    global l
    global opciones3
    global profesiones3
    global e1
    global e2
    global e3
    e3 = opciones3.get()
        #if e3 not in l:
    if e3 not in l:
        messagebox.showerror("Advertencia", "Corrija su respuesta")
    else:
        print(e1,e2,e3)
        messagebox.showerror("Advertencia", "Ingresadas correctamente")
        delete3()
                
    prof=open("datos voc.csv","a")
    prof.write(e1)
    prof.write(",")
    prof.write(e2)
    prof.write(",")  
    prof.write(e3)
    prof.write(",")        
    prof.close()

#   Tercera ventana, muestra si las opciones fueron compatible o no.
def atrventana3(suma):
    global otra_ventana2
    global a
    global e1
    global e2
    global e3
    #suma = 115
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
        x1 = "la primera opcion es compatible"
        comp_1 = Label(otra_ventana2, text = x1, bg = "#213141",  font = ("Times",20, "italic"), fg = "white")
        comp_1.place(x = 180, y = 50)
    else:
        x1="la primera opcion no es compatible"
        comp_1 = Label(otra_ventana2, text = x1, bg = "#213141",  font = ("Times",20, "italic"), fg = "white")
        comp_1.place(x = 180, y = 50)
    if e2 in a:
        x2="la segunda opcion es compatible"
        comp_2 = Label(otra_ventana2, text = x2, bg = "#213141",  font = ("Times",20, "italic"), fg = "white")
        comp_2.place(x = 180, y = 150)
    else:
        x2="la segunda opcion no es compatible"
        comp_2 = Label(otra_ventana2, text = x2, bg = "#213141",  font = ("Times",20, "italic"), fg = "white")
        comp_2.place(x = 180, y = 150)
    if e3 in a:
        x3="la tercera opcion es compatible"
        comp_3 = Label(otra_ventana2, text = x3, bg = "#213141",  font = ("Times",20, "italic"), fg = "white")
        comp_3.place(x = 180, y = 250)
    else:
        x3="la tercera opcion no es compatible"
        comp_3 = Label(otra_ventana2, text = x3, bg = "#213141",  font = ("Times",20, "italic"), fg = "white")
        comp_3.place(x = 180, y = 250)
    
#   sugerencias compatibles    
def funsuger():
    for i in range(len(a)-1):
        print(a[i])
        sug=open("datos voc.csv","a")
        sug.write(a[i])
        sug.write(",")
        sug.close()
    sug=open("datos voc.csv","a")
    x=len(a)
    sug.write(a[x-1]+'\n')
    sug.close()
    datos=pd.read_csv("datos voc.csv", names=['cedula','nombre','edad','genero','categoria','elec_1','elec_2','elec_3','comp_1','comp_2','comp_3','comp_4','comp_5','comp_6','comp_7'])
    root = Toplevel(otra_ventana2)
    table = Text(root, height=180, width=200)
    table.insert(INSERT, datos.to_string())
    table.pack()
def print_categoria(suma):
    global boton_A
    global boton_B
    global boton_C
    global preguntas_label
    global global_label2
    global boton_siguiente
    global boton_imagen
    preguntas_label.destroy()
    global_label2.destroy()
    boton_A.destroy()
    boton_B.destroy()
    boton_C.destroy()
    boton_siguiente.destroy()
    boton_imagen.place(x = 200, y = 500)
    puntaje = 'Su puntaje fue: ' + str(suma)
    global_label3 = Label(text = puntaje, bg = "#213141",  font = ("Times",20, "italic"), fg = "white")
    global_label3.place(x = 50, y = 300)
    if suma <= 70:
        resultado = 'Usted pertenece a la categoria: ARTISTA'
        c= 'ARTISTA'
        cat=open("voc.csv","a")
        cat.write(c +'\n')
        cat.close()
        global_label3 = Label(text = resultado, bg = "#213141",  font = ("Times",20, "italic"), fg = "white")
        global_label3.place(x = 10, y = 300)
        return c
    elif suma <= 92:
        resultado = 'Usted pertenece a la categoria: SOCIALES'
        c='SOCIALES'
        cat=open("voc.csv","a")
        cat.write(c +'\n')
        cat.close()
        global_label3 = Label(text = resultado, bg = "#213141",  font = ("Times",20, "italic"), fg = "white")
        global_label3.place(x = 10, y = 300)
        return c
    elif suma <= 114:
        resultado = 'Usted pertenece a la categoria: INVESTIGADOR'
        c= 'INVESTIGADOR'
        cat=open("voc.csv","a")
        cat.write(c +'\n')
        cat.close()
        global_label3 = Label(text = resultado, bg = "#213141",  font = ("Times",20, "italic"), fg = "white")
        global_label3.place(x = 10, y = 300)
        return c
    elif suma <= 136:
        resultado = 'Usted pertenece a la categoria: REALISTA'
        c= 'REALISTA'
        cat=open("voc.csv","a")
        cat.write(c +'\n')
        cat.close()
        global_label3 = Label(text = resultado, bg = "#213141",  font = ("Times",20, "italic"), fg = "white")
        global_label3.place(x = 10, y = 300)
        return 'REALISTA'
    elif suma <= 158:
        resultado = 'Usted pertenece a la categoria: EMPRENDEDOR'
        c= 'EMPRENDEDOR'
        cat=open("voc.csv","a")
        cat.write(c +'\n')
        cat.close()
        global_label3 = Label(text = resultado, bg = "#213141",  font = ("Times",20, "italic"), fg = "white")
        global_label3.place(x = 50, y = 80)
        return c
    else:
        resultado = 'Usted pertenece a la categoria: CONVENCIONAL'
        c = 'CONVENCIONAL'
        cat=open("voc.csv","a")
        cat.write(c +'\n')
        cat.close()
        global_label3 = Label(text = resultado, bg = "#213141",  font = ("Times",20, "italic"), fg = "white")
        global_label3.place(x = 50, y = 80)
        return c

#   función para abrir las recomendaciones.
def funcion():
    global otra_ventana
    global opciones
    global profesiones
    global boton_opciones
    a="artes escenicas"
    b="cine y television"
    c="danza" 
    d="arquitectura"
    e="bellas artes"
    f="diseño" 
    g="publicidad"  
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
    mywindow.iconify()
    otra_ventana = Toplevel()
    otra_ventana.title('Tabla')
    otra_ventana.configure(bg = "#213141")
    otra_ventana.geometry('800x600')
    boton_opciones = Button(otra_ventana,text = "Ok", width = "10", height = "2", command=print_compatibilidad , bg = "burlywood", font = ("Times",16, "bold"))
    boton_opciones.place(x = 180, y = 500)
    label_a = Label(otra_ventana,text = a, bg = "#213141",  font = ("Times",8, "italic"), fg = "white")
    label_a.place(x = 250, y = 5)
    label_b = Label(otra_ventana,text = b, bg = "#213141",  font = ("Times",8, "italic"), fg = "white")
    label_b.place(x = 250, y = 20)
    label_c = Label(otra_ventana,text = c, bg = "#213141",  font = ("Times",8, "italic"), fg = "white")
    label_c.place(x = 250, y = 35)
    label_d = Label(otra_ventana,text = d, bg = "#213141",  font = ("Times",8, "italic"), fg = "white")
    label_d.place(x = 250, y = 50)
    label_e = Label(otra_ventana,text = e, bg = "#213141",  font = ("Times",8, "italic"), fg = "white")
    label_e.place(x = 250, y = 65)
    label_f = Label(otra_ventana,text = f, bg = "#213141",  font = ("Times",8, "italic"), fg = "white")
    label_f.place(x = 250, y = 80)
    label_g = Label(otra_ventana,text = g, bg = "#213141",  font = ("Times",8, "italic"), fg = "white")
    label_g.place(x = 250, y = 105)
    label_h = Label(otra_ventana,text = h, bg = "#213141",  font = ("Times",8, "italic"), fg = "white")
    label_h.place(x = 250, y = 120)
    label_i = Label(otra_ventana,text = i, bg = "#213141",  font = ("Times",8, "italic"), fg = "white")
    label_i.place(x = 250, y = 135)
    label_j = Label(otra_ventana,text = j, bg = "#213141",  font = ("Times",8, "italic"), fg = "white")
    label_j.place(x = 250, y = 150)
    label_k = Label(otra_ventana,text = k, bg = "#213141",  font = ("Times",8, "italic"), fg = "white")
    label_k.place(x = 250, y = 175)
    label_l = Label(otra_ventana,text = l, bg = "#213141",  font = ("Times",8, "italic"), fg = "white")
    label_l.place(x = 250, y = 190)
    label_m = Label(otra_ventana,text = m, bg = "#213141",  font = ("Times",8, "italic"), fg = "white")
    label_m.place(x = 250, y = 205)
    label_n = Label(otra_ventana,text = n, bg = "#213141",  font = ("Times",8, "italic"), fg = "white")
    label_n.place(x = 250, y = 220)
    label_o = Label(otra_ventana,text = o, bg = "#213141",  font = ("Times",8, "italic"), fg = "white")
    label_o.place(x = 250, y = 235)
    label_p = Label(otra_ventana,text = p, bg = "#213141",  font = ("Times",8, "italic"), fg = "white")
    label_p.place(x = 250, y = 250)
    label_q = Label(otra_ventana,text = q, bg = "#213141",  font = ("Times",8, "italic"), fg = "white")
    label_q.place(x = 250, y = 275)
    label_r = Label(otra_ventana,text = r, bg = "#213141",  font = ("Times",8, "italic"), fg = "white")
    label_r.place(x = 250, y = 300)
    label_s = Label(otra_ventana,text = s, bg = "#213141",  font = ("Times",8, "italic"), fg = "white")
    label_s.place(x = 250, y = 315)
    label_t = Label(otra_ventana,text = t, bg = "#213141",  font = ("Times",8, "italic"), fg = "white")
    label_t.place(x = 250, y = 330)
    label_u = Label(otra_ventana,text = u, bg = "#213141",  font = ("Times",8, "italic"), fg = "white")
    label_u.place(x = 250, y = 345)
    label_v = Label(otra_ventana,text = v, bg = "#213141",  font = ("Times",8, "italic"), fg = "white")
    label_v.place(x = 250, y = 360)
    label_w = Label(otra_ventana,text = w, bg = "#213141",  font = ("Times",8, "italic"), fg = "white")
    label_w.place(x = 250, y = 375)
    label_x = Label(otra_ventana,text = x, bg = "#213141",  font = ("Times",8, "italic"), fg = "white")
    label_x.place(x = 250, y = 390)
    label_y = Label(otra_ventana,text = y, bg = "#213141",  font = ("Times",8, "italic"), fg = "white")
    label_y.place(x = 250, y = 405)
    label_z = Label(otra_ventana,text = z, bg = "#213141",  font = ("Times",8, "italic"), fg = "white")
    label_z.place(x = 250, y = 420)
    global_label = Label(otra_ventana,text = "Escoja tres de las profesiones mostradas y escribala en minusculas:" , bg = "#213141",  font = ("Times",10, "italic"), fg = "white")
    global_label.place(x = 200, y = 450)
    opciones = StringVar()
    profesiones = Entry(otra_ventana, textvariable = opciones, bg = "saddlebrown", width = "30", font=("Helvetica",14,"bold")) 
    profesiones.place(x=70,y=490)
    #print_compatibilidad(total)
    

def salir():
    respuesta = messagebox.askyesno("¿Abandonar?", "¿Está seguro que desea salir del cuestionario?\n Se perderán todos los datos\n")
    if respuesta == True:
        mywindow.destroy()

#Creación del formulario-------------------------------------------------
mywindow = Tk()
mywindow.geometry("700x600")
mywindow.title("Formulario")
mywindow.resizable(False,False)
mywindow.config(background = "#213141")
main_title = Label(text = "Análisis Aptitudinal y Profesional", font = ("Cambria", 20), bg = "sienna", fg = "black", width = "500", height = "2")
main_title.pack()
global_label = Label(text = "Por favor, llene los siguientes datos:", bg = "#213141",  font = ("Times",20, "italic"), fg = "white")
global_label.place(x = 50, y = 80)
cedula_label = Label(text = "Cédula o Documento de Identidad:", bg = "#213141",  font = ("Times",20, "italic"), fg = "white")
cedula_label.place(x = 180, y = 190)
username_label = Label(text = "Nombres y Apellidos:", bg = "#213141",  font = ("Times",20, "italic"), fg = "white")
username_label.place(x = 180, y = 250)
edad_label = Label(text = "Edad:", bg = "#213141",  font = ("Times",20, "italic"), fg = "white")
edad_label.place(x = 180, y = 310)
genero_label = Label(text = "Género(1: masculino, 0: femenino):", bg = "#213141",  font = ("Times",20, "italic"), fg = "white")
genero_label.place(x = 180, y = 370)

cedula = StringVar()
username = StringVar()
edad = StringVar()
genero = StringVar()

cedula_entry = Entry(mywindow, textvariable = cedula, bg = "saddlebrown", width = "30", font=("Helvetica",14,"bold")) 
username_entry = Entry(mywindow, textvariable = username, bg = "saddlebrown", width = "30", font=("Helvetica",14,"bold"))
edad_entry = Entry(mywindow, textvariable = edad, bg = "saddlebrown", width = "30", font=("Helvetica",14,"bold"))
genero_entry = Entry(mywindow, textvariable = genero, bg = "saddlebrown", width = "30", font=("Helvetica",14,"bold"))

cedula_entry.place(x = 200, y = 222)
username_entry.place(x = 200, y = 282)
edad_entry.place(x = 200, y =342)
genero_entry.place(x = 200, y = 402)

respuesta_A = "A. Si, me encuentro muy a gusto en los trabajos con movilidad."
respuesta_B = "B. Prefiero trabajos fijos y sin movimiento."
respuesta_C = "C. No, no me gusta viajar."
var = IntVar()
boton_A = Radiobutton(mywindow, text=respuesta_A, variable=var, value=1,
                  command=onclick)

boton_B = Radiobutton(mywindow, text=respuesta_B, variable=var, value=2,
                  command=onclick)

boton_C = Radiobutton(mywindow, text=respuesta_C, variable=var, value=3,
                  command=onclick)

boton_salir = Button(mywindow,text = "Salir", width = "5", height = "2", command=salir, bg = "burlywood", font = ("Times",16, "bold"))
boton_siguiente = Button(mywindow,text = "Siguiente", width = "10", height = "2", command=checkbox_clicked , bg = "burlywood", font = ("Times",16, "bold"))
boton_opciones = Button(mywindow,text = "Ok", width = "10", height = "2", command=print_compatibilidad , bg = "burlywood", font = ("Times",16, "bold"))
boton_imagen = Button(mywindow,text = "Recomendaciones", width = "15", height = "2", command=funcion , bg = "burlywood", font = ("Times",16, "bold"))
boton_atras = Button(mywindow,text = "Atrás", width = "10", height = "2", command=salir, bg = "burlywood", font = ("Times",16, "bold"))
boton_atras.place(x = 180, y = 450)
#validacion
boton_listo = Button(mywindow,text = "Listo", width = "10", height = "2", command=validacion , bg = "burlywood", font = ("Times",16, "bold"))
boton_listo.place(x = 400, y = 450)
mywindow.mainloop()

