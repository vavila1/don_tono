import sys
import os

# Obtén la ruta del directorio actual
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Agrega el directorio 'views' al sys.path
directorio_views = os.path.join(directorio_actual, "..", "views")
sys.path.append(directorio_views)

# Importa las funciones necesarias desde view_tienda
from view_tienda import *
from tkinter import *
    
def root_almacen():
    global root_almacen
    root_almacen = Toplevel()
    root_almacen.geometry("400x300")
    root_almacen.title("Area de almacen")
    button_return = Button(root_almacen, text="regresar", width=15, bg="red",command=root_almacen_return).grid(row=1, column=1)
    if root_almacen: 
        root.withdraw()

def root_material():
    global root_material
    root_material = Toplevel()
    root_material.geometry("400x300")
    root_material.title("Area de material")
    button_return = Button(root_material, text="regresar", width=15, bg="red",command=root_material_return).grid(row=1, column=1)
    if root_material: 
        root.withdraw()
    
def root_tienda():
    
    frame_tienda = Frame(root, background="#C5C6C7")  # Agrega el relleno deseado entre los botones
    frame_tienda.grid(row=0, column=1, sticky="nsew")  
    root_mostrar_tienda()
    button_crear_tienda = Button(frame_tienda, text="Crear tienda", width=15, bg="#66FCF1", command=root_crear_tienda).grid(row=1, column=0, padx=5, pady=5)
    button_mostrar_tienda = Button(frame_tienda, text="Mostrar tiendas", width=15, bg="#66FCF1", command=root_mostrar_tienda).grid(row=1, column=1, padx=5, pady=5)
    button_editar_tienda = Button(frame_tienda, text="Editar tienda", width=15, bg="#66FCF1", command=root_editar_tienda).grid(row=2, column=0, padx=5, pady=5)
    button_eliminar_tienda = Button(frame_tienda, text="Eliminar tienda", width=15, bg="#66FCF1",command=root_eliminar_tienda).grid(row=2, column=1, padx=5, pady=5)
        
def root_crear_tienda():
    global frame_crear_tienda
    frame_crear_tienda = Frame(root, background="#6c648B")  # Agrega el relleno deseado entre los botones
    if frame_mostrar_tienda:
        frame_mostrar_tienda.destroy()
    elif frame_editar_tienda:
        frame_editar_tienda.destroy()
    elif frame_eliminar_tienda:
        frame_eliminar_tienda.destroy()
    frame_crear_tienda.grid(row=0, column=2, sticky="nsew") 
    #Crear los witgets que se utilizaran
    input_nombre_tienda = Entry(frame_crear_tienda)
    input_direccion_tienda = Entry(frame_crear_tienda)
    text_nombre_tienda = Label(frame_crear_tienda, text="Inserta el nombre de la tienda: ")
    text_direccion_tienda = Label(frame_crear_tienda, text="Inserta la direccion de la tienda: ")
    button_crear_tienda = Button(frame_crear_tienda, text="Guardar", width=15, bg="#66FCF1", command=lambda: command_crear_tienda(input_nombre_tienda.get(),input_direccion_tienda.get()))
    #Mostrar los witgets en la ventana
    text_nombre_tienda.pack(padx=5, pady=5)
    input_nombre_tienda.pack(padx=5, pady=5)
    text_direccion_tienda.pack(padx=5, pady=5)
    input_direccion_tienda.pack(padx=5, pady=5)
    button_crear_tienda.pack(padx=5, pady=5)

def command_crear_tienda(nombre, direccion):
    frame_crear_tienda.destroy()
    crear_tienda(nombre,direccion)
    root_mostrar_tienda()
    
def root_mostrar_tienda():
    #Creacion de la ventana root_crear_tienda
    global frame_mostrar_tienda
    if frame_crear_tienda:
        frame_crear_tienda.destroy()
    elif frame_editar_tienda:
        frame_editar_tienda.destroy()
    elif frame_eliminar_tienda:
        frame_eliminar_tienda.destroy()
    frame_mostrar_tienda = Frame(root, background="#6c648B")  # Agrega el relleno deseado entre los botones
    frame_mostrar_tienda.grid(row=0, column=2, sticky="nsew")
    #Crear los witgets que se utilizaran
    tabla_datos_tienda = ttk.Treeview(frame_mostrar_tienda, columns=("Nombre","Dirección","Fecha"))
    tabla_datos_tienda.column("#0", width=80)
    tabla_datos_tienda.column(0, width=80)
    tabla_datos_tienda.column(1, width=80)
    tabla_datos_tienda.column(2, width=130)
    tabla_datos_tienda.heading("#0", text="ID", anchor=CENTER)
    tabla_datos_tienda.heading(0, text="Nombre", anchor=CENTER)
    tabla_datos_tienda.heading(1, text="Dirección", anchor=CENTER)
    tabla_datos_tienda.heading(2, text="Fecha", anchor=CENTER)
    #Logica de tiendas
    tiendas = tienda.leer_tiendas()
    for row in tiendas:
        ids=str(row[0])
        nombre=str(row[1])
        direccion=str(row[2])
        fecha=str(row[4])
        tabla_datos_tienda.insert('', 'end', text=ids, values=[nombre, direccion, fecha])
    #Mostrar los witgets en la ventana
    tabla_datos_tienda.pack()
    button_actualizar_tabla = Button(frame_mostrar_tienda, text="Actualizar", width=15, bg="#66FCF1", command=root_mostrar_tienda).pack(padx=5, pady=5)

def root_editar_tienda():
    global frame_editar_tienda
    if frame_crear_tienda:
        frame_crear_tienda.destroy()
    elif frame_mostrar_tienda:
        frame_mostrar_tienda.destroy()
    elif frame_eliminar_tienda:
        frame_eliminar_tienda.destroy()
    frame_editar_tienda = Frame(root, background="#6c648B")  # Agrega el relleno deseado entre los botones
    frame_editar_tienda.grid(row=0, column=2, sticky="nsew")
    #Crear los witgets que se utilizaran
    input_id_tienda = Entry(frame_editar_tienda)
    input_nombre_tienda = Entry(frame_editar_tienda)
    input_direccion_tienda = Entry(frame_editar_tienda)
    text_id_tienda = Label(frame_editar_tienda, text="Inserta el id de la tienda: ")
    text_nombre_tienda = Label(frame_editar_tienda, text="Inserta el nuevo nombre de la tienda: ")
    text_direccion_tienda = Label(frame_editar_tienda, text="Inserta la nueva direccion de la tienda: ")
    button_crear_tienda = Button(frame_editar_tienda, text="Actualizar", width=15, bg="#66FCF1", command=lambda: command_editar_tienda(input_id_tienda.get(),input_nombre_tienda.get(),input_direccion_tienda.get()))
    #Mostrar los witgets en la ventana
    text_id_tienda.pack(padx=5, pady=5)
    input_id_tienda.pack(padx=5, pady=5)
    text_nombre_tienda.pack(padx=5, pady=5)
    input_nombre_tienda.pack(padx=5, pady=5)
    text_direccion_tienda.pack(padx=5, pady=5)
    input_direccion_tienda.pack(padx=5, pady=5)
    button_crear_tienda.pack(padx=5, pady=5)

def command_editar_tienda(ids, nombre, direccion):
    frame_editar_tienda.destroy()
    editar_tienda(ids,nombre,direccion)
    root_mostrar_tienda()
    
def root_eliminar_tienda():
    global frame_eliminar_tienda
    if frame_crear_tienda:
        frame_crear_tienda.destroy()
    elif frame_mostrar_tienda:
        frame_mostrar_tienda.destroy()
    elif frame_editar_tienda:
        frame_editar_tienda.destroy()
    frame_eliminar_tienda = Frame(root, background="#6c648B")  # Agrega el relleno deseado entre los botones
    frame_eliminar_tienda.grid(row=0, column=2, sticky="nsew")
    #Crear los witgets que se utilizaran
    input_id_tienda = Entry(frame_eliminar_tienda)
    text_id_tienda = Label(frame_eliminar_tienda, text="Inserta el id de la tienda: ")
    button_eliminar_tienda = Button(frame_eliminar_tienda, text="Eliminar", width=15, bg="#66FCF1", command=lambda: command_eliminar_tienda(input_id_tienda.get()))
    #Mostrar los witgets en la ventana
    text_id_tienda.pack(padx=5, pady=5)
    input_id_tienda.pack(padx=5, pady=5)
    button_eliminar_tienda.pack(padx=5, pady=5)

def command_eliminar_tienda(ids):
    frame_eliminar_tienda.destroy()
    eliminar_tienda(ids)
    root_mostrar_tienda()
    
def root_almacen_return():
    root_almacen.destroy()  
    root.iconify()
    root.deiconify()

def root_material_return():
    root_material.destroy()  
    root.iconify()
    root.deiconify()
           

root = Tk()
root.title("Aplicacion Don Tono")
root.geometry("750x300")
frame_principal = Frame(root, background="#1F2833")  # Agrega el relleno deseado entre los botones
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
frame_principal.grid(row=0, column=0, sticky="nsew")
frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_columnconfigure(0, weight=1)
button_almacen = Button(frame_principal, text="Area de almacen", width=15, bg="#66FCF1", command=root_almacen).pack(padx=5,pady=5)
button_material = Button(frame_principal, text="Area de materiales", width=15, bg="#66FCF1", command=root_material).pack(padx=5,pady=5)
button_tienda = Button(frame_principal, text="Area de tienda", width=15, bg="#66FCF1", command=root_tienda).pack(padx=5,pady=5)

frame_mostrar_tienda = False
frame_crear_tienda = False
frame_editar_tienda = False
frame_eliminar_tienda = False

root.mainloop()