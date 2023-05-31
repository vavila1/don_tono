import sys
import os
directorio_actual = os.getcwd()
directorio_models = os.path.dirname(directorio_actual)
directorio_models+= "/models"
sys.path.append(directorio_models)
import model_tipo_operacion as tipo_operacion
import tkinter as tk
from tkinter import ttk
def crear_frame_mostrar_tipos_de_operacion(ventana_menu_principal,frame_menu_tipos_de_operacion):
    def regresar_mostrar_tipos_de_operacion(frame_editar_tipos_de_operacion):
        frame_editar_tipos_de_operacion.pack_forget()
        frame_mostrar_tipos_de_operacion.pack()
    def guardar_valores(valores,var_nombre_tipo_de_operacion_editar,tabla,frames):
        id = valores[0]
        valores = list(valores)
        valores = []
        valores.append(var_nombre_tipo_de_operacion_editar.get())
        resultado = tipo_operacion.editar_tipo_operacion(id,valores)
        tipo_operaciones = tipo_operacion.leer_tipo_operaciones()
        if(resultado == True):
            print("Se ha editado con exito el tipo de operacion")
            tabla.delete(*tabla.get_children())
            for i, fila in enumerate(tipo_operaciones):
                tabla.insert("", "end",values=(fila[0],fila[1],fila[3],fila[4]))
            frames[1].pack_forget()
            frames[0].pack()
        else:
            print("Ha ocurrido un error al editar el tipo de operacion")
    def crear_frame_editar_tipo_operacion(ventana_menu_principal,frame_mostrar_tipos_de_operacion,tabla):
        frame_mostrar_tipos_de_operacion.pack_forget()
        frame_editar_tipos_de_operacion = tk.Frame(ventana_menu_principal)
        btn_regresar_mostrar_tipos_de_operacion = tk.Button(frame_editar_tipos_de_operacion,text="Regresar",command=lambda: regresar_mostrar_tipos_de_operacion(frame_editar_tipos_de_operacion))
        btn_regresar_mostrar_tipos_de_operacion.pack()
        item = tabla.focus()
        valores = tabla.item(item,"values")
        #Se crean variables de control
        var_nombre_tipo_de_operacion_editar = tk.StringVar(value=valores[1])
        #Se crean las entradas de crear tipo operacion
        entry_editar_tipo_operacion = tk.Entry(frame_editar_tipos_de_operacion, textvariable=var_nombre_tipo_de_operacion_editar)
        entry_editar_tipo_operacion.pack(side="top",padx=200,pady=10)
        btn_guardar_tipos_operacion = tk.Button(frame_editar_tipos_de_operacion, text="Guardar",command=lambda: guardar_valores(valores,var_nombre_tipo_de_operacion_editar,tabla,frames=[frame_mostrar_tipos_de_operacion,frame_editar_tipos_de_operacion]))
        btn_guardar_tipos_operacion.pack(side="top",padx=200,pady=10)
        frame_editar_tipos_de_operacion.pack()
    def eliminar_tipo_de_operacion(tabla):
        item = tabla.focus()
        valores = tabla.item(item, "values")
        id = valores[0]
        resultado = tipo_operacion.eliminar_tipo_operacion(id)
        tipo_operaciones = tipo_operacion.leer_tipo_operaciones()
        if(resultado == True):
            print("Se ha eliminado con exito el tipo de operacion")
             # Eliminar los elementos existentes en la tabla
            tabla.delete(*tabla.get_children())
            for i, fila in enumerate(tipo_operaciones):
                tabla.insert("", "end",values=(fila[0],fila[1],fila[3],fila[4]))
        else:
            print("Ha ocurrido un error al elimintar el tipo de operacion")
    def mostrar_tabla_tipos_de_operaciones(frame_mostrar_tipos_de_operacion):
        tipo_operaciones = tipo_operacion.leer_tipo_operaciones()
        tabla = ttk.Treeview(frame_mostrar_tipos_de_operacion, columns=("ID", "Nombre","Creado","Actualizado"),show="headings")
        tabla.heading("ID", text="ID")
        tabla.heading("Nombre", text="Nombre")
        tabla.heading("Creado", text="Creado")
        tabla.heading("Actualizado", text="Actualizado")
        
        for i, fila in enumerate(tipo_operaciones):
            tabla.insert("", "end",values=(fila[0],fila[1],fila[3],fila[4]))
        
        tabla.pack()
        btn_editar_tipos_operacion = tk.Button(frame_mostrar_tipos_de_operacion,text="Editar",command=lambda: crear_frame_editar_tipo_operacion(ventana_menu_principal,frame_mostrar_tipos_de_operacion,tabla))
        btn_editar_tipos_operacion.pack(side="left",padx = 100)
        btn_eliminar_tipos_operacion = tk.Button(frame_mostrar_tipos_de_operacion,text="Eliminar",command=lambda: eliminar_tipo_de_operacion(tabla))
        btn_eliminar_tipos_operacion.pack(side="left",padx=100)
    def regresar(frame_menu_tipos_de_operacion):
        frame_mostrar_tipos_de_operacion.pack_forget()
        frame_menu_tipos_de_operacion.pack()
    frame_menu_tipos_de_operacion.pack_forget()
    frame_mostrar_tipos_de_operacion = tk.Frame(ventana_menu_principal)
    btn_regresar_menu_tipos_de_operacion = tk.Button(frame_mostrar_tipos_de_operacion,text="Regresar",command=lambda: regresar(frame_menu_tipos_de_operacion))
    btn_regresar_menu_tipos_de_operacion.pack()
    mostrar_tabla_tipos_de_operaciones(frame_mostrar_tipos_de_operacion)
    frame_mostrar_tipos_de_operacion.pack()


def crear_frame_crear_tipos_de_operacion(ventana_menu_principal,frame_menu_tipos_de_operacion):
    def crear_tipo_operacion():
        nombre_tipo_operacion = var_nombre_tipo_de_operacion.get()
        if(nombre_tipo_operacion == ""):
            return
        valores = []
        valores.append(nombre_tipo_operacion)
        valores.append(1)
        resultado = tipo_operacion.crear_tipo_operacion(valores)
        if(resultado == True):
            print("Se ha registrado con exito la tienda")
        else:
            print("Ha ocurrido un error al registrar la tienda")
    def regresar(frame_menu_tipos_de_operacion):
        frame_crear_tipos_de_operacion.pack_forget()
        frame_menu_tipos_de_operacion.pack()
    frame_menu_tipos_de_operacion.pack_forget()
    frame_crear_tipos_de_operacion = tk.Frame(ventana_menu_principal)
    btn_regresar_menu_tipos_de_operacion = tk.Button(frame_crear_tipos_de_operacion,text="Regresar",command=lambda: regresar(frame_menu_tipos_de_operacion))
    btn_regresar_menu_tipos_de_operacion.pack()
    label_nombre_tipo_de_operacion = tk.Label(frame_crear_tipos_de_operacion, text="Nombre del tipo de operacion:")
    label_nombre_tipo_de_operacion.pack()
    #Se crean variables de control
    var_nombre_tipo_de_operacion = tk.StringVar()
    frame_crear_tipos_de_operacion.pack()
    #Se crean las entradas de crear tipo operacion
    entry_usuario = tk.Entry(frame_crear_tipos_de_operacion, textvariable=var_nombre_tipo_de_operacion)
    entry_usuario.pack()
    btn_guardar_tipos_operacion = tk.Button(frame_crear_tipos_de_operacion, text="Guardar", command=crear_tipo_operacion)
    btn_guardar_tipos_operacion.pack()


def crear_frame_menu_tipos_de_operacion(ventana_menu_principal,frame_menu_principal,regresar_de_menu_tipos_de_operacion):
    frame_menu_principal.pack_forget()
    frame_menu_tipos_de_operacion = tk.Frame(ventana_menu_principal)
    btn_regresar_menu_principal = tk.Button(frame_menu_tipos_de_operacion,text="Regresar al menu principal",command=lambda: regresar_de_menu_tipos_de_operacion(frame_menu_tipos_de_operacion,frame_menu_principal))
    btn_regresar_menu_principal.pack()
    btn_crear_tipo_operacion = tk.Button(frame_menu_tipos_de_operacion, text="1.- Crear Tipo de Operacion",command=lambda: crear_frame_crear_tipos_de_operacion(ventana_menu_principal,frame_menu_tipos_de_operacion))
    btn_crear_tipo_operacion.pack(side="top",padx=200,pady=10)
    btn_mostrar_tipos_operacion = tk.Button(frame_menu_tipos_de_operacion,text="2.- Mostrar Tipos de Operacion",command=lambda: crear_frame_mostrar_tipos_de_operacion(ventana_menu_principal,frame_menu_tipos_de_operacion))
    btn_mostrar_tipos_operacion.pack(side="top",padx=200,pady=10)
    frame_menu_tipos_de_operacion.pack()