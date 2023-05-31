import sys
import os
directorio_actual = os.getcwd()
directorio_models = os.path.dirname(directorio_actual)
directorio_models+= "/models"
sys.path.append(directorio_models)
import model_tipo_operacion as tipo_operacion
import tkinter as tk
from tkinter import ttk
def validarOpcion(mensaje):
  try:
    variable = int(input(mensaje))
    return variable
  except:
    print("Debes ingresar un numero que corresponda a la opción elegida")
    return False
def iterarValidacion(mensaje):
    opcion = False
    while(opcion == False):
        opcion = validarOpcion(mensaje)
    return opcion
def crear_tipo_operacion():
    nombre_tipo_operacion = var_nombre_tipo_de_operacion.get()
    valores = []
    valores.append(nombre_tipo_operacion)
    valores.append(1)
    resultado = tipo_operacion.crear_tipo_operacion(valores)
    if(resultado == True):
        print("Se ha registrado con exito la tienda")
    else:
        print("Ha ocurrido un error al registrar la tienda")
def editar_tipo_operacion():
        def guardar(valores):
            id = valores[0]
            valores = list(valores)
            valores = []
            valores.append(var_nombre_tipo_de_operacion_editar.get())
            print(valores)
            resultado = tipo_operacion.editar_tipo_operacion(id,valores)
            print(resultado)
            if(resultado == True):
                print("Se ha editado con exito el tipo de operacion")
            else:
                print("Ha ocurrido un error al editar el tipo de operacion")
        item = tabla.focus()  # Obtener el elemento seleccionado
        valores = tabla.item(item, "values")  # Obtener los valores de la fila seleccionada
        ventana_editar_tipo_de_operaciones()
        #Se crean variables de control
        var_nombre_tipo_de_operacion_editar = tk.StringVar(value=valores[1])
        #Se crean las entradas de crear tipo operacion
        global entry_editar_tipo_operacion
        entry_editar_tipo_operacion = tk.Entry(frame_editar_tipos_operacion, textvariable=var_nombre_tipo_de_operacion_editar)
        entry_editar_tipo_operacion.pack(side="top",padx=200,pady=10)
        global btn_guardar_tipos_operacion
        btn_guardar_tipos_operacion = tk.Button(frame_editar_tipos_operacion, text="Guardar",command=lambda: guardar(valores))
        btn_guardar_tipos_operacion.pack(side="top",padx=200,pady=10)
def eliminar_tipo_de_operacion():
    item = tabla.focus()
    valores = tabla.item(item, "values")
    id = valores[0]
    resultado = tipo_operacion.eliminar_tipo_operacion(id)
    if(resultado == True):
        print("Se ha eliminado con exito el tipo de operacion")
    else:
        print("Ha ocurrido un error al elimintar el tipo de operacion")
def mostrar_tipo_operaciones():
    tipo_operaciones = tipo_operacion.leer_tipo_operaciones()
    global tabla  # Declarar la variable como global
    tabla = ttk.Treeview(frame_mostrar_tipos_operacion, columns=("ID", "Nombre","Creado","Actualizado"),show="headings")
    tabla.heading("ID", text="ID")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Creado", text="Creado")
    tabla.heading("Actualizado", text="Actualizado")
    
    for i, fila in enumerate(tipo_operaciones):
        tabla.insert("", "end",values=(fila[0],fila[1],fila[3],fila[4]))
    

    tabla.pack()
    global btn_editar_tipos_operacion
    global btn_eliminar_tipos_operacion
    btn_editar_tipos_operacion = tk.Button(frame_mostrar_tipos_operacion,text="Editar",command=editar_tipo_operacion)
    btn_editar_tipos_operacion.pack(side="left",padx = 100)
    btn_eliminar_tipos_operacion = tk.Button(frame_mostrar_tipos_operacion,text="Eliminar",command=eliminar_tipo_de_operacion)
    btn_eliminar_tipos_operacion.pack(side="left",padx=100)
"""def editar_tipo_operacion():
    print(var_nombre_tipo_de_operacion_editar.get())
    valor_viejo = tipo_operacion.leer_tipo_operacion(id)
    print(valor_viejo)
    if(valor_viejo == []):
        print("No existe el dato en la base de datos")
        return
    valores = [valor_viejo[1]]
    inputs = []
    opcion1 = iterarValidacion("Ingresa 1 en caso de querer editar el nombre de tipo de operacion \nIngresa 2 para pasar al siguiente dato\n")
    if(opcion1 == 1):
        nombre = input("Escribe el nuevo nombre\n")
        valores[0] = nombre
        inputs.append(1)
    else:
        inputs.append(2)

    if(inputs[0] == 1):
        resultado = tipo_operacion.editar_tipo_operacion(id,valores)
        if(resultado == True):
            print("Se ha editado con exito la tienda")
        else:
            print("Ocurrio un error al editar la tienda")
    else:
        print("No hay nada que editar")"""
"""def eliminar_tipo_operacion(id):
    resultado = tipo_operacion.leer_tipo_operacion(id)
    if(resultado == []):
        print("No existe en la base de datos")
        return
    resultado = tipo_operacion.eliminar_tipo_operacion(id)
    if(resultado == True):
        print("Se ha eliminado el material con exito")
    else:
        print("Hubo un error al eliminar la tienda")
opcion = 0
while(opcion!=5):
    print("MENU\n1.- Crear Tipo de Operacion\n2.- Mostrar Tipos de Operaciones\n3.- Editar Tipo de Operacion\n4.- Eliminar Tipo Operacion\n5.- Salir")
    opcion = validarOpcion("Ingresa el numero que  corresponda a la opcion deseada\n")
    if(opcion==1):
        crear_tipo_operacion()
    elif(opcion == 2):
        mostrar_tipo_operacion()
    elif(opcion == 3):
        mostrar_tipo_operacion()
        id = iterarValidacion("Escribe el ID correspondiente del tipo de operacion a editar\n")
        editar_tipo_operacion(id)
    elif(opcion == 4):
        mostrar_tipo_operacion()
        id = iterarValidacion("Escribe el ID correspondiente del tipo de operacion a eliminar\n")
        eliminar_tipo_operacion(id)
    elif(opcion==5):
        print("Saliendo del programa...")
    else:
        opcion = 5
        print("Esa opcion no esta registrada. Saliendo del programa...")"""


def ventana_crear_tipo_de_operacion():
    frame_principal.pack_forget()
    frame_crear_tipos_operacion.pack()
def ventana_mostrar_tipo_de_operaciones():
    frame_principal.pack_forget()
    frame_mostrar_tipos_operacion.pack()
    mostrar_tipo_operaciones()
def ventana_editar_tipo_de_operaciones():
    frame_mostrar_tipos_operacion.pack_forget()
    frame_editar_tipos_operacion.pack()
    limpiar_tabla()
def volver_a_ventana_principal_mostrar_tipos_operacion():
    frame_mostrar_tipos_operacion.pack_forget()
    frame_principal.pack()
    limpiar_tabla()
def volver_a_ventana_principal_crear_tipos_operacion():
    frame_crear_tipos_operacion.pack_forget()
    frame_principal.pack()
def volver_a_ventana_principal_editar_tipos_operacion():
    frame_editar_tipos_operacion.pack_forget()
    frame_mostrar_tipos_operacion.pack()
    mostrar_tipo_operaciones()
    global entry_editar_tipo_operacion
    entry_editar_tipo_operacion.destroy()
    global btn_guardar_tipos_operacion
    btn_guardar_tipos_operacion.destroy()
def limpiar_tabla():
    global tabla  # Declarar la variable como global
    if tabla is not None:
        tabla.destroy()  # Elimina la tabla por completo
        tabla = None  # Establecer la variable como None
    global btn_eliminar_tipos_operacion
    btn_eliminar_tipos_operacion.destroy()
    global btn_editar_tipos_operacion
    btn_editar_tipos_operacion.destroy()
def salir():
    ventana_menu_tipos_operaciones.quit()
# Crear la ventana principal
tabla = None
ventana_menu_tipos_operaciones = tk.Tk()
ventana_menu_tipos_operaciones.geometry("600x600")
#Crear Tabla
tabla = None
# Crear el frame de la ventana principal
frame_principal = tk.Frame(ventana_menu_tipos_operaciones)

# Crear el botón "Ventana Personalizada"
btn_crear_tipo_operacion = tk.Button(frame_principal, text="1.- Crear Tipo de Operacion", command=ventana_crear_tipo_de_operacion)
btn_crear_tipo_operacion.pack(side="top",padx=200,pady=10)
btn_mostrar_tipos_operacion = tk.Button(frame_principal,text="2.- Mostrar Tipos de Operacion",command=ventana_mostrar_tipo_de_operaciones)
btn_mostrar_tipos_operacion.pack(side="top",padx=200,pady=10)
btn_salir = tk.Button(frame_principal,text="Salir",command=salir)
btn_salir.pack(side="top",padx=200,pady=10)
# Crear el frame de crear_tipos_operacion
frame_crear_tipos_operacion = tk.Frame(ventana_menu_tipos_operaciones)
btn_ventana_personalizada = tk.Button(frame_crear_tipos_operacion,text="Regresar",command=volver_a_ventana_principal_crear_tipos_operacion)
btn_ventana_personalizada.pack(side="top",padx=200,pady=10)
label_nombre_tipo_de_operacion = tk.Label(frame_crear_tipos_operacion, text="Nombre del tipo de operacion:")
label_nombre_tipo_de_operacion.pack(side="top",padx=200,pady=10)
#Se crean variables de control
var_nombre_tipo_de_operacion = tk.StringVar()
#Se crean las entradas de crear tipo operacion
entry_usuario = tk.Entry(frame_crear_tipos_operacion, textvariable=var_nombre_tipo_de_operacion)
entry_usuario.pack()
btn_guardar_tipos_operacion = tk.Button(frame_crear_tipos_operacion, text="Guardar", command=crear_tipo_operacion)
btn_guardar_tipos_operacion.pack()
# Crear el frame de mostrar_tipos_operacion
frame_mostrar_tipos_operacion = tk.Frame(ventana_menu_tipos_operaciones)
btn_regresar_mostrar_tipos_operacion = tk.Button(frame_mostrar_tipos_operacion,text="Regresar",command=volver_a_ventana_principal_mostrar_tipos_operacion)
btn_regresar_mostrar_tipos_operacion.pack()
#Crear el Frame de editar_tipo_operacion
frame_editar_tipos_operacion = tk.Frame(ventana_menu_tipos_operaciones)
btn_regresar_editar_tipos_operacion = tk.Button(frame_editar_tipos_operacion,text="Regresar",command=volver_a_ventana_principal_editar_tipos_operacion)
btn_regresar_editar_tipos_operacion.pack()
label_nombre_tipo_de_operacion = tk.Label(frame_editar_tipos_operacion, text="Nombre del tipo de operacion:")
label_nombre_tipo_de_operacion.pack(side="top",padx=200,pady=10)
# Mostrar el frame principal inicialmente
frame_principal.pack()

# Iniciar el bucle principal de la ventana principal
ventana_menu_tipos_operaciones.mainloop()