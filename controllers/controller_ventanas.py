import sys
import os
"""
# Obtén la ruta del directorio actual
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Agrega el directorio 'views' al sys.path
directorio_views = os.path.join(directorio_actual, "..", "views")
sys.path.append(directorio_views)
directorio_models = os.path.join(directorio_actual,"..","models")
sys.path.append(directorio_models)
"""
directorio_actual = os.getcwd()
directorio_models = os.path.dirname(directorio_actual)
directorio_models+= "/models"
sys.path.append(directorio_models)
directorio_actual = os.getcwd()
directorio_models = os.path.dirname(directorio_actual)
directorio_models+= "/views"
sys.path.append(directorio_models)
# Importa las funciones necesarias desde view_tienda
from view_tienda import *
from tkinter import *
#Para mac
import model_venta as venta
    
def root_tienda():
    frame_tienda = Frame(root, background="#C5C6C7")  # Agrega el relleno deseado entre los botones
    frame_tienda.grid(row=0, column=1, sticky="nsew")  
    root_mostrar_tienda()
def root_reportes_empleado():
    frame_reportes_empleado = Frame(root, background="#C5C6C7")  # Agrega el relleno deseado entre los botones
    frame_reportes_empleado.grid(row=0, column=1, sticky="nsew")  
    root_mostrar_reportes_empleado()

def root_reportes_material():
    frame_reportes_material = Frame(root, background="#C5C6C7")  # Agrega el relleno deseado entre los botones
    frame_reportes_material.grid(row=0, column=1, sticky="nsew")  
    root_mostrar_reportes_material()
    
def root_crear_tienda():
    global frame_crear_tienda
    frame_crear_tienda = Frame(root, background="#6c648B")  # Agrega el relleno deseado entre los botones
    if frame_editar_tienda:
        frame_editar_tienda.destroy()
    frame_crear_tienda.grid(row=0, column=2, sticky="nsew") 
    #Crear los witgets que se utilizaran
    input_nombre_tienda = Entry(frame_crear_tienda)
    input_direccion_tienda = Entry(frame_crear_tienda)
    text_nombre_tienda = Label(frame_crear_tienda, text="Inserta el nombre de la tienda: ")
    text_direccion_tienda = Label(frame_crear_tienda, text="Inserta la direccion de la tienda: ")
    button_crear_tienda = Button(frame_crear_tienda, text="Guardar", width=15, bg="#66FCF1", command=lambda: command_crear_tienda(input_nombre_tienda.get(),input_direccion_tienda.get()))
    button_cancelar = Button(frame_crear_tienda, text="Cancelar", width=15, bg="#66FCF1", command=root_mostrar_tienda)
    #Mostrar los witgets en la ventana
    text_nombre_tienda.pack(padx=5, pady=5)
    input_nombre_tienda.pack(padx=5, pady=5)
    text_direccion_tienda.pack(padx=5, pady=5)
    input_direccion_tienda.pack(padx=5, pady=5)
    button_crear_tienda.pack(padx=5, pady=5)
    button_cancelar.pack(padx=5, pady=5)

def command_crear_tienda(nombre, direccion):
    frame_crear_tienda.destroy()
    crear_tienda(nombre,direccion)
    root_mostrar_tienda()
    
def root_mostrar_tienda():
    #Creacion de la ventana root_crear_tienda
    global frame_mostrar_tienda
    frame_mostrar_tienda = Frame(root, background="#6c648B")  # Agrega el relleno deseado entre los botones
    frame_mostrar_tienda.grid(row=0, column=2, sticky="nsew")
    #Crear los witgets que se utilizaran
    tabla_datos_tienda = ttk.Treeview(frame_mostrar_tienda, columns=("ID","Nombre","Dirección","Fecha"),show="headings")
    tabla_datos_tienda.column(0, width=80)
    tabla_datos_tienda.column(1, width=80)
    tabla_datos_tienda.column(2, width=80)
    tabla_datos_tienda.column(3, width=130)
    tabla_datos_tienda.heading(0, text="ID", anchor=CENTER)
    tabla_datos_tienda.heading(1, text="Nombre", anchor=CENTER)
    tabla_datos_tienda.heading(2, text="Dirección", anchor=CENTER)
    tabla_datos_tienda.heading(3, text="Fecha", anchor=CENTER)
    #Logica de tiendas
    tiendas = tienda.leer_tiendas()
    for row in tiendas:
        ids=str(row[0])
        nombre=str(row[1])
        direccion=str(row[2])
        fecha=str(row[4])
        tabla_datos_tienda.insert('', 'end', values=[ids,nombre, direccion, fecha])
    
    #Mostrar los witgets en la ventana
    tabla_datos_tienda.pack()
    button_crear_tienda = Button(frame_mostrar_tienda, text="Agregar tienda", width=15, bg="#66FCF1", command=root_crear_tienda).pack(side="left" ,padx=5, pady=5)
    button_editar_tienda = Button(frame_mostrar_tienda, text="Editar tienda", width=15, bg="#66FCF1", command=lambda: root_editar_tienda(tabla_datos_tienda)).pack(side="left" ,padx=5, pady=5)
    button_eliminar_tienda = Button(frame_mostrar_tienda, text="Eliminar", width=15, bg="#66FCF1", command=lambda: command_eliminar_tienda(tabla_datos_tienda)).pack(side="left" ,padx=5, pady=5)
def root_mostrar_reportes_empleado():
    #Creacion de la ventana root_crear_tienda
    global frame_mostrar_reportes_empleado
    frame_mostrar_reportes_empleado = Frame(root, background="#6c648B")  # Agrega el relleno deseado entre los botones
    frame_mostrar_reportes_empleado.grid(row=0, column=2, sticky="nsew")
    #Crear los witgets que se utilizaran
    tabla_reportes_empleado = ttk.Treeview(frame_mostrar_reportes_empleado, columns=("ID","Nombre","Apellido Paterno","Total Ventas"),show="headings")
    tabla_reportes_empleado.column(0, width=80)
    tabla_reportes_empleado.column(1, width=80)
    tabla_reportes_empleado.column(2, width=80)
    tabla_reportes_empleado.column(3, width=130)
    tabla_reportes_empleado.heading(0, text="ID", anchor=CENTER)
    tabla_reportes_empleado.heading(1, text="Nombre", anchor=CENTER)
    tabla_reportes_empleado.heading(2, text="Apellido Paterno", anchor=CENTER)
    tabla_reportes_empleado.heading(3, text="Total Ventas", anchor=CENTER)
    reportes_empleado = venta.reporte_ventas_empleados()
    for row in reportes_empleado:
        tabla_reportes_empleado.insert('','end',values=[row[0],row[1],row[2],row[3]])
    #Mostrar los witgets en la ventana
    tabla_reportes_empleado.pack()
def root_mostrar_reportes_material():
    #Creacion de la ventana root_crear_tienda
    global frame_mostrar_reportes_material
    frame_mostrar_reportes_material = Frame(root, background="#6c648B")  # Agrega el relleno deseado entre los botones
    frame_mostrar_reportes_material.grid(row=0, column=2, sticky="nsew")
    #Crear los witgets que se utilizaran
    tabla_reportes_material = ttk.Treeview(frame_mostrar_reportes_material, columns=("ID","Nombre","Total Ventas"),show="headings")
    tabla_reportes_material.column(0, width=80)
    tabla_reportes_material.column(1, width=150)
    tabla_reportes_material.column(2, width=80)
    tabla_reportes_material.heading(0, text="ID", anchor=CENTER)
    tabla_reportes_material.heading(1, text="Nombre", anchor=CENTER)
    tabla_reportes_material.heading(2, text="Total Ventas", anchor=CENTER)
    reportes_material = venta.reporte_ventas_materiales()
    for row in reportes_material:
        tabla_reportes_material.insert('','end',values=[row[0],row[1],row[2]])
    #Mostrar los witgets en la ventana
    tabla_reportes_material.pack()

def root_editar_tienda(tabla):
    global frame_editar_tienda
    item = tabla.focus()
    valores = tabla.item(item,"values")
    id = valores[0]
    if frame_crear_tienda:
        frame_crear_tienda.destroy()
    frame_editar_tienda = Frame(root, background="#6c648B")  # Agrega el relleno deseado entre los botones
    frame_editar_tienda.grid(row=0, column=2, sticky="nsew")
    #Crear los witgets que se utilizaran
    input_nombre_tienda = Entry(frame_editar_tienda)
    input_direccion_tienda = Entry(frame_editar_tienda)
    text_nombre_tienda = Label(frame_editar_tienda, text="Inserta el nuevo nombre de la tienda: ")
    text_direccion_tienda = Label(frame_editar_tienda, text="Inserta la nueva direccion de la tienda: ")
    button_crear_tienda = Button(frame_editar_tienda, text="Actualizar", width=15, bg="#66FCF1", command=lambda: command_editar_tienda(id,input_nombre_tienda.get(),input_direccion_tienda.get()))
    button_cancelar = Button(frame_editar_tienda, text="Cancelar", width=15, bg="#66FCF1", command=root_mostrar_tienda)
    #Mostrar los witgets en la ventana
    text_nombre_tienda.pack(padx=5, pady=5)
    input_nombre_tienda.pack(padx=5, pady=5)
    text_direccion_tienda.pack(padx=5, pady=5)
    input_direccion_tienda.pack(padx=5, pady=5)
    button_crear_tienda.pack(padx=5, pady=5)
    button_cancelar.pack(padx=5, pady=5)

def command_editar_tienda(ids, nombre, direccion):
    frame_editar_tienda.destroy()
    editar_tienda(ids,nombre,direccion)
    root_mostrar_tienda()

def command_eliminar_tienda(tabla):
    item = tabla.focus()
    valores = tabla.item(item,"values")
    id = valores[0]
    eliminar_tienda(id)
    root_mostrar_tienda()
           
root = Tk()
root.title("Aplicacion Don Tono")
root.geometry("750x300")
frame_principal = Frame(root, background="#1F2833")  # Agrega el relleno deseado entre los botones
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
frame_principal.grid(row=0, column=0, sticky="nsew")
frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_columnconfigure(0, weight=1)
#button_almacen = Button(frame_principal, text="Area de almacen", width=15, bg="#66FCF1", command=root_almacen).pack(padx=5,pady=5)
#button_material = Button(frame_principal, text="Area de materiales", width=15, bg="#66FCF1", command=root_material).pack(padx=5,pady=5)
button_tienda = Button(frame_principal, text="Area de tienda", width=15, bg="#66FCF1", command=root_tienda).pack(padx=5,pady=5)
button_reportes_empleado = Button(frame_principal, text="Reportes Empleado", width=15, bg="#66FCF1", command=root_reportes_empleado).pack(padx=5,pady=5)
button_reportes_material = Button(frame_principal, text="Reportes Material", width=15, bg="#66FCF1", command=root_reportes_material).pack(padx=5,pady=5)

frame_mostrar_tienda = False
frame_crear_tienda = False
frame_editar_tienda = False
frame_eliminar_tienda = False

root.mainloop()