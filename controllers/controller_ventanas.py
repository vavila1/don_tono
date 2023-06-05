import sys
import os

# Obtén la ruta del directorio actual
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Agrega el directorio 'views' al sys.path
directorio_views = os.path.join(directorio_actual, "..", "views")
sys.path.append(directorio_views)
"""
directorio_actual = os.getcwd()
directorio_views = os.path.dirname(directorio_actual)
directorio_views+= "/views"
sys.path.append(directorio_views)
"""
# Importa las funciones necesarias desde view_tienda
from view_tienda import *
from view_empleado import *
from view_cuenta import *
from tkinter import *
from tkinter import ttk
#-------------------Tiendas-----------------------------
        
def root_crear_tienda():
    global frame_crear_tienda
    frame_crear_tienda = Frame(root, background="#6c648B")  # Agrega el relleno deseado entre los botones
    frame_crear_tienda.grid(row=0, column=1, sticky="nsew") 
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
    #Creacion del frame root_mostrar_tienda
    global frame_mostrar_tienda
    frame_mostrar_tienda = Frame(root, background="#C5C6C7")  # Agrega el relleno deseado entre los botones
    frame_mostrar_tienda.grid(row=0, column=1, sticky="nsew")
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

def root_editar_tienda(tabla):
    global frame_editar_tienda
    item = tabla.focus()
    valores = tabla.item(item,"values")
    id = valores[0]
    frame_editar_tienda = Frame(root, background="#6c648B")  # Agrega el relleno deseado entre los botones
    frame_editar_tienda.grid(row=0, column=1, sticky="nsew")
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

#----------------------Empleados------------------------

def root_mostrar_empleado():
    #Creacion de la ventana root_mostrar_empleado
    global frame_mostrar_empleado
    frame_mostrar_empleado = Frame(root, background="#C5C6C7")  # Agrega el relleno deseado entre los botones
    frame_mostrar_empleado.grid(row=0, column=1, sticky="nsew")
    #Crear los witgets que se utilizaran
    tabla_datos_empleado = ttk.Treeview(frame_mostrar_empleado, columns=("Id","Nombre","Apellido_paterno","Apellido_materno", "Correo","Lugar_trabajo" , "fecha"),show="headings")
    tabla_datos_empleado.column(0, width=50)
    tabla_datos_empleado.column(1, width=130)
    tabla_datos_empleado.column(2, width=130)
    tabla_datos_empleado.column(3, width=130)
    tabla_datos_empleado.column(4, width=130)
    tabla_datos_empleado.column(5, width=130)
    tabla_datos_empleado.column(6, width=130)
    tabla_datos_empleado.heading(0, text="Id", anchor=CENTER)
    tabla_datos_empleado.heading(1, text="Nombre", anchor=CENTER)
    tabla_datos_empleado.heading(2, text="Apellido_paterno", anchor=CENTER)
    tabla_datos_empleado.heading(3, text="Apellido_materno", anchor=CENTER)
    tabla_datos_empleado.heading(4, text="Correo", anchor=CENTER)
    tabla_datos_empleado.heading(5, text="Lugar_trabajo", anchor=CENTER)
    tabla_datos_empleado.heading(6, text="Fecha", anchor=CENTER)
    #Logica de tiendas
    empleados = empleado.leer_empleados()
    for row in empleados:
        ids=str(row[0])
        nombre=str(row[3])
        Apellido_paterno=str(row[4])
        Apellido_materno=str(row[5])
        correo=str(row[1])
        lugar_trabajo=str(row[2])
        fecha=str(row[6])
        tabla_datos_empleado.insert('', 'end', values=[ids,nombre, Apellido_paterno, Apellido_materno, correo,lugar_trabajo, fecha])
    
    #Mostrar los witgets en la ventana
    tabla_datos_empleado.pack()
    button_crear_empleado = Button(frame_mostrar_empleado, text="Agregar empleado", width=15, bg="#66FCF1", command=root_crear_empleado).pack(side="left" ,padx=5, pady=5)
    button_editar_tienda = Button(frame_mostrar_empleado, text="Editar empleado", width=15, bg="#66FCF1", command=lambda: root_editar_empleado(tabla_datos_empleado)).pack(side="left" ,padx=5, pady=5)
    button_eliminar_tienda = Button(frame_mostrar_empleado, text="Eliminar empleado", width=15, bg="#66FCF1", command=lambda: command_eliminar_empleado(tabla_datos_empleado)).pack(side="left" ,padx=5, pady=5)
    
def root_crear_empleado():
    global frame_crear_empleado
    frame_crear_empleado = Frame(root, background="#6c648B")
    frame_crear_empleado.grid(row=0, column=1, sticky="nsew") 
    
    # Crear los widgets que se utilizarán
    input_correo = Entry(frame_crear_empleado)
    input_password = Entry(frame_crear_empleado, show="*")
    drop_rol = ttk.Combobox(frame_crear_empleado, values=["Administrador", "Almacenista", "Vendedor"])
    drop_rol.current(0)
    global tiendas
    tiendas = tienda.leer_tiendas()
    nombre = []
    for row in tiendas:
        nombre.append(str(row[1]))
    
    drop_lugar_trabajo = ttk.Combobox(frame_crear_empleado, values=nombre)
    drop_lugar_trabajo.current(0)
    input_nombre = Entry(frame_crear_empleado)
    input_apellido_paterno = Entry(frame_crear_empleado)
    input_apellido_materno = Entry(frame_crear_empleado)
    text_input_correo = Label(frame_crear_empleado, text="Inserta su correo electrónico: ",justify=LEFT)
    text_input_password = Label(frame_crear_empleado, text="Inserta su contraseña: ",justify=LEFT)
    text_select_rol = Label(frame_crear_empleado, text="Selecciona su rol ",justify=LEFT)
    text_input_nombre = Label(frame_crear_empleado, text="Inserta su nombre: ",justify=LEFT)
    text_input_apellido_paterno = Label(frame_crear_empleado, text="Inserta su apellido paterno: ",justify=LEFT)
    text_input_apellido_materno = Label(frame_crear_empleado, text="Inserta su apellido materno: ",justify=LEFT)
    text_select_lugar_trabajo = Label(frame_crear_empleado, text="Selecciona tu lugar de trabajo ",justify=LEFT)
    button_crear_empleado = Button(frame_crear_empleado, text="Guardar", width=15, bg="#66FCF1", command=lambda: command_crear_empleado(input_correo.get(), input_password.get(), drop_rol.get(), input_nombre.get(), input_apellido_paterno.get(), input_apellido_materno.get(), drop_lugar_trabajo.get()))
    button_cancelar = Button(frame_crear_empleado, text="Cancelar", width=15, bg="#66FCF1", command=root_mostrar_empleado)

    # Mostrar los widgets en la ventana
    text_input_nombre.pack(padx=5, pady=5)
    input_nombre.pack(padx=5, pady=5)
    text_input_apellido_paterno.pack(padx=5, pady=5)
    input_apellido_paterno.pack(padx=5, pady=5)
    text_input_apellido_materno.pack(padx=5, pady=5)
    input_apellido_materno.pack(padx=5, pady=5)
    text_input_correo.pack(padx=5, pady=5)
    input_correo.pack(padx=5, pady=5)
    text_input_password.pack(padx=5, pady=5)
    input_password.pack(padx=5, pady=5)
    text_select_rol.pack(padx=5, pady=5)
    drop_rol.pack(padx=5, pady=5)
    text_select_lugar_trabajo.pack(padx=5, pady=5)
    drop_lugar_trabajo.pack(padx=5, pady=5)
    button_crear_empleado.pack(padx=5, pady=5)
    button_cancelar.pack(padx=5, pady=5)

def command_crear_empleado(correo, password, rol, nombre, apellido_paterno, apellido_materno, lugar_trabajo):
    frame_crear_empleado.destroy()
    if rol == "Administrador":
        id_rol=2
    elif rol == "Almacenista":
        id_rol=1
    elif rol == "Vendedor":
        id_rol=3
    lugar_trabajo_id = None
    for tienda in tiendas:
        if tienda[1] == lugar_trabajo:
            lugar_trabajo_id = tienda[0]
            break
    crear_cuenta(correo,password,id_rol,nombre, apellido_paterno, apellido_materno,lugar_trabajo_id)
    root_mostrar_empleado()  

def root_editar_empleado(tabla):
    global frame_editar_empleado
    item = tabla.focus()
    valores = tabla.item(item,"values")
    id = valores[0]
    frame_editar_empleado = Frame(root, background="#6c648B")
    frame_editar_empleado.grid(row=0, column=1, sticky="nsew") 
    # Crear los widgets que se utilizarán
    global mistiendas
    mistiendas = tienda.leer_tiendas()
    nombre = []
    for row in mistiendas:
        nombre.append(str(row[1]))
    drop_lugar_trabajo = ttk.Combobox(frame_editar_empleado, values=nombre)
    drop_lugar_trabajo.current(0)
    input_nombre = Entry(frame_editar_empleado)
    input_apellido_paterno = Entry(frame_editar_empleado)
    input_apellido_materno = Entry(frame_editar_empleado)
    text_input_nombre = Label(frame_editar_empleado, text="Inserta su nombre: ",justify=LEFT)
    text_input_apellido_paterno = Label(frame_editar_empleado, text="Inserta su apellido paterno: ",justify=LEFT)
    text_input_apellido_materno = Label(frame_editar_empleado, text="Inserta su apellido materno: ",justify=LEFT)
    text_select_lugar_trabajo = Label(frame_editar_empleado, text="Selecciona tu lugar de trabajo ",justify=LEFT)
    button_crear_empleado = Button(frame_editar_empleado, text="Actualizar", width=15, bg="#66FCF1", command=lambda: command_editar_empleado(id,drop_lugar_trabajo.get(),input_nombre.get(),input_apellido_paterno.get(),input_apellido_materno.get()))
    button_cancelar = Button(frame_editar_empleado, text="Cancelar", width=15, bg="#66FCF1", command=root_mostrar_empleado)

    # Mostrar los widgets en la ventana
    text_input_nombre.pack(padx=5, pady=5)
    input_nombre.pack(padx=5, pady=5)
    text_input_apellido_paterno.pack(padx=5, pady=5)
    input_apellido_paterno.pack(padx=5, pady=5)
    text_input_apellido_materno.pack(padx=5, pady=5)
    input_apellido_materno.pack(padx=5, pady=5)
    text_select_lugar_trabajo.pack(padx=5, pady=5)
    drop_lugar_trabajo.pack(padx=5, pady=5)
    button_crear_empleado.pack(padx=5, pady=5)
    button_cancelar.pack(padx=5, pady=5)

def command_editar_empleado(id,lugar_trabajo,nombre, apellido_paterno,apellido_materno):
    frame_editar_empleado.destroy()
    lugar_trabajo_id = None
    for tienda in mistiendas:
        if tienda[1] == lugar_trabajo:
            lugar_trabajo_id = tienda[0]
            break
    editar_empleado(id,nombre,apellido_paterno,apellido_materno,lugar_trabajo_id)
    root_mostrar_empleado()

def command_eliminar_empleado(tabla):
    item = tabla.focus()
    valores = tabla.item(item,"values")
    id = valores[0]
    eliminar_empleado(id)
    root_mostrar_empleado()
#-------------------Menu principal------------------           
root = Tk()
root.title("Aplicacion Don Tono")
root.geometry("1200x700")
frame_principal = Frame(root, background="#1F2833")  # Agrega el relleno deseado entre los botones
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
frame_principal.grid(row=0, column=0, sticky="nsew")
frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_columnconfigure(0, weight=1)
button_tienda = Button(frame_principal, text="Tiendas", width=15, bg="#66FCF1", command=root_mostrar_tienda).pack(side="top",padx=5,pady=5)
button_empleado = Button(frame_principal, text="Empleados", width=15, bg="#66FCF1", command=root_mostrar_empleado).pack(side="top",padx=5,pady=5)

root.mainloop()