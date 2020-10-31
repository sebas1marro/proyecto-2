from tkinter import *
from mostrar_datos.carga_datos import carga_dic, export_dic
import numpy as np

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
    export_dic(ruta_encuesta, encuestados)
    return documento

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
        preguntas_label = pregunta 
        print(pregunta)
        
        for respuestas in preguntas[pregunta]:
            print('\t', respuestas)
        print('\nSeleccione A, B o C')
        respuesta = val_resp('----> ')
        respuesta = resp_num(respuesta)
        """
        encuestados[cedula]['respuestas'].append(respuesta)
    export_dic(ruta_encuesta, encuestados)
"""
#preguntar("./datos/datos.json","./datos/respuestas.json", 101406421)

def result(cedula, ruta_encuesta):
    encuestados = carga_dic(ruta_encuesta)
    lista_num = encuestados[cedula]['respuestas']
    total = np.sum(lista_num)
    categ = print_categoria(total)
    encuestados['categoria'] = categ
    export_dic(ruta_encuesta, encuestados)

    #Funcion Principal
def main(opcion):
    ruta = "./datos/datos.json"
    ruta_preguntas = "./datos/respuestas.json"
    if opcion == "arg":
        cedula = identity
        preguntar(ruta, ruta_preguntas, cedula)
        result(cedula, ruta)

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
    #boton1.pack()
    generador()
    valorpreguntas = 1
    botonescheck()
    
def botonescheck():
    global boton_A
    global boton_B
    global boton_C
    global preguntas_label
    global valorpreguntas
    encuestados = carga_dic("./datos/datos.json")
    preguntas = carga_dic("./datos/respuestas.json")
    contador = 0
    listapreguntas = list()
    listarespuestas = list()   
    for pregunta in preguntas:
        respuesta = ''
        listapreguntas.append(pregunta)
        for respuestas in preguntas[pregunta]:
            listarespuestas.append(respuestas)
    #return listapreguntas[0]
    #return listarespuestas[0]
    while valorpreguntas == 1:   
        preguntas_label = Label(text = listapreguntas[contador],  bg = "#213141",  font = ("Times",20, "italic"), fg = "white")
        contador += 1
        valorpreguntas = 0
        
    preguntas_label.place(x = 30, y = 150)
#botonescheck()
def onclick():
     # Function to call when user clicks on button
    print("Checkbox is clicked!")
    print("value : ",botonA_valor.get())
def generador():    
    boton_A.place(x = 100, y = 250)
    boton_B.place(x = 100, y = 320)
    boton_C.place(x = 100, y = 390)
    
def checkbox_clicked():
    global valorpreguntas
    global valorrespuestas
    global botonA_valor
    global botonB_valor
    global botonC_valor
    #valorpreguntas = 0
    if botonA_valor == 1:
        botonB_valor = 0
        botonC_valor = 0
        valorpreguntas = 1
        botonescheck()
        resp_num('A')
        messagebox.showerror("Advertencia", "1era escogida")
        """
    boton_A.invoke()
    messagebox.showerror("Advertencia", botonA_valor.get())
    """
    if botonB_valor == 1:
        botonA_valor = 0
        botonC_valor = 0
        valorpreguntas = 1
        botonescheck()
        #resp_num('B')
        messagebox.showerror("Advertencia", "2da escogida")
    if botonC_valor == 1:
        botonA_valor = 0
        botonB_valor = 0
        valorpreguntas = 1
        botonescheck()
        #resp_num('C')
        messagebox.showerror("Advertencia", "3era escogida")
    if botonA_valor and botonB_valor and botonC_valor == 0:
        valorpreguntas = 0
        messagebox.showerror("Advertencia", "Escoja una respuesta")

#   funcion pensada para abrir otro formulario en el inicio.
def funcion():
    otra_ventana = Toplevel(mywindow)
    mywindow.iconify()

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

botonA_valor = IntVar()
botonB_valor = IntVar()
botonC_valor = IntVar()

respuesta_A = "A. Si, me encuentro muy a gusto en los trabajos con movilidad."
respuesta_B = "B. Prefiero trabajos fijos y sin movimiento."
respuesta_C = "C. No, no me gusta viajar."
boton_A = Checkbutton(mywindow,text = respuesta_A,variable = botonA_valor)#,command = onclick)
boton_B = Checkbutton(mywindow,text = respuesta_B,variable = botonB_valor)#,command = onclick)
boton_C = Checkbutton(mywindow,text = respuesta_C,variable = botonC_valor)#,command = onclick)
boton_salir = Button(mywindow,text = "Salir", width = "5", height = "2", command=salir, bg = "burlywood", font = ("Times",16, "bold"))
boton_siguiente = Button(mywindow,text = "Siguiente", width = "10", height = "2", command=checkbox_clicked , bg = "burlywood", font = ("Times",16, "bold"))
boton1 = Button(mywindow, text = "prueba",  command = generador)

"""
ventana_inicio = Tk()
ventana_inicio.geometry("700x600")
ventana_inicio.title("Bienvenido")
ventana_inicio.resizable(False,False)
ventana_inicio.configure(background = "sienna") 

boton = Button(mywindow, text="Abrir otra ventana", command=funcion)
boton.pack()
mywindow.mainloop()
"""

boton_atras = Button(mywindow,text = "Atrás", width = "10", height = "2", command=salir, bg = "burlywood", font = ("Times",16, "bold"))
boton_atras.place(x = 180, y = 450)
boton_listo = Button(mywindow,text = "Listo", width = "10", height = "2", command=validacion , bg = "burlywood", font = ("Times",16, "bold"))
boton_listo.place(x = 400, y = 450)
mywindow.mainloop()

