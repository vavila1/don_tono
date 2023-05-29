import tkinter as tk

"""# Crear una instancia de la ventana principal
ventana = tk.Tk()

# Configurar propiedades de la ventana
ventana.title("Menu")
ventana.geometry("400x300")

# Agregar elementos a la ventana
etiqueta = tk.Label(ventana, text="¡Hola, mundo!")
etiqueta.pack()

boton = tk.Button(ventana, text="Haz clic")
boton.pack()

# Iniciar el bucle de eventos de la ventana
ventana.mainloop()"""
import tkinter as tk
import sys
import os
directorio_actual = os.getcwd()
directorio_models = os.path.dirname(directorio_actual)
directorio_models+= "/models"
sys.path.append(directorio_models)
import model_material as material
import model_tipo_unidad as tipo_unidad
def mostrar_materiales():
    materiales = material.leer_materiales()
    print("ID\tNombre\tPrecio\tTipo de Unidad\tFecha\n")
    for row in materiales:
        unidad = tipo_unidad.leer_tipo_unidad(row[1])
        print(str(row[0])+"\t"+str(row[2])+"\t"+str(row[3])+"\t"+str(unidad[1])+"\t"+str(row[5]))
"""import tkinter as tk

def seleccionar():
    seleccion = menu_var.get()
    id_seleccion = None
    for producto in productos:
        if producto[1] == seleccion:
            id_seleccion = producto[0]
            break
    print(id_seleccion)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Menu")
ventana.geometry("400x300")
# Lista de productos [ID, Nombre]
productos = [[1, "Coca Cola"], [2, "Fanta"], [3, "Sprite"]]

# Obtener los nombres de los productos
nombres_productos = [producto[1] for producto in productos]

# Variable para almacenar la selección
menu_var = tk.StringVar(ventana)
menu_var.set(nombres_productos[0])

# Crear el menú desplegable
menu = tk.OptionMenu(ventana, menu_var, *nombres_productos)
menu.pack()

# Crear el botón "Seleccionar"
boton = tk.Button(ventana, text="Seleccionar", command=seleccionar)
boton.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()"""
"""import tkinter as tk

def cambiar_a_ventana_personalizada():
    frame_principal.grid_remove()
    frame_ventana_personalizada.grid()
def volver_a_ventana_principal():
    frame_ventana_personalizada.grid_remove()
    frame_principal.grid()

# Crear la ventana principal
ventana_principal = tk.Tk()

# Crear el frame de la ventana principal
frame_principal = tk.Frame(ventana_principal)
frame_principal.grid(row=0, column=0)

# Crear el botón "Ventana Personalizada"
btn_ventana_personalizada = tk.Button(frame_principal, text="Ventana Personalizada", command=cambiar_a_ventana_personalizada)
btn_ventana_personalizada.pack()

# Crear el frame de la ventana personalizada
frame_ventana_personalizada = tk.Frame(ventana_principal)
label_ventana_personalizada = tk.Label(frame_ventana_personalizada, text="Estás en otra ventana")
btn_ventana_personalizada = tk.Button(frame_ventana_personalizada,text="Regresar",command=volver_a_ventana_principal)
btn_ventana_personalizada.pack()
label_ventana_personalizada.pack()

# Mostrar el frame principal inicialmente
frame_principal.grid()

# Iniciar el bucle principal de la ventana principal
ventana_principal.mainloop()"""


"""import tkinter as tk

def iniciar_sesion():
    usuario = var_usuario.get()
    contrasena = var_contrasena.get()
    print("Usuario:", usuario)
    print("Contraseña:", contrasena)

ventana = tk.Tk()

var_usuario = tk.StringVar()
var_contrasena = tk.StringVar()

label_usuario = tk.Label(ventana, text="Usuario:")
label_usuario.pack()

entry_usuario = tk.Entry(ventana, textvariable=var_usuario)
entry_usuario.pack()

label_contrasena = tk.Label(ventana, text="Contraseña:")
label_contrasena.pack()

entry_contrasena = tk.Entry(ventana, show="*", textvariable=var_contrasena)
entry_contrasena.pack()

btn_iniciar_sesion = tk.Button(ventana, text="Iniciar Sesión", command=iniciar_sesion)
btn_iniciar_sesion.pack()

ventana.mainloop()"""







