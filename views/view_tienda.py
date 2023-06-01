import sys
import os
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

directorio_actual = os.getcwd()
directorio_models = os.path.join(directorio_actual, "models")
sys.path.append(directorio_models)



try:
    import model_tienda as tienda
except ImportError as e:
    print("Error al importar 'model_tienda':", str(e))

def validarOpcion(mensaje):
  try:
    variable = int(input(mensaje))
    return variable
  except:
    print("Debes ingresar un numero que corresponda a la opción elegida")
    return False

def crear_tienda(nombre,direccion):
    valores = [nombre,direccion,1]
    resultado = tienda.crear_tienda(valores)
    if(resultado == True):
        showinfo(message="Se ha registrado con exito la tienda", title="Proceso exitoso")
    else:
        showerror(message="Ha ocurrido un error al registrar la tienda", title="Proceso fallido")
    

    
def editar_tienda(id,nombre, direccion):
    valor_viejo = tienda.leer_tienda(id)
    valores = [valor_viejo[1],valor_viejo[2]]
    valores[0] = nombre
    valores[1] = direccion
    resultado = tienda.editar_tienda(id,valores)
    if(resultado == True):
        showinfo(message="Se ha editado con exito la tienda", title="Proceso exitoso")
    else:
        showerror(message="Ha ocurrido un error al editar la tienda", title="Proceso fallido")



    
def eliminar_tienda(id):
    confirmacion = askyesno("Confirmacion de eliminacion", "¿Estás seguro de que deseas eliminar la tienda?")
    if confirmacion:
        resultado = tienda.eliminar_tienda(id)
        if(resultado == True):
            showinfo(message="Se ha eliminado con exito la tienda", title="Proceso exitoso")
        else:
            showerror(message="Ha ocurrido un error al eliminar la tienda", title="Proceso fallido")
    else:
        showinfo(message="El proceso fue cancelado", title="Cancelar")


