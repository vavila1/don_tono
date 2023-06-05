import sys
import os

# Obtén la ruta del directorio actual
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Agrega el directorio 'views' al sys.path
directorio_models = os.path.join(directorio_actual, "..", "models")
sys.path.append(directorio_models)

import model_empleado as empleado
import model_cuenta as cuenta
import model_almacen as almacen
import model_tienda as tienda
import model_rol as rol
from tkinter.messagebox import *
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

def Almacenes():
    almacenes = almacen.leer_almacenes()
    if(almacenes == []):
        print("No existen almacenes en la base de datos para asignarle al empleado")
        return 0
    for i, row in enumerate(almacenes):
        print(str(row[0])+".- "+row[1])
    id_almacen = iterarValidacion("Ingresa el numero que represente el almacen a asignar\n")
    return id_almacen
def Tiendas():
    tiendas = tienda.leer_tiendas()
    if(tiendas == []):
        print("No existen tiendas en la base de datos para asignarle al empleado")
        return 0
    for i, row in enumerate(tiendas):
        print(str(row[0])+".- "+row[1])
    id_tienda = iterarValidacion("Ingresa el numero que represente la tienda a asignar\n")
    return id_tienda
def Roles():
    roles = rol.leer_roles()
    if(roles == []):
        print("No existen roles en la base de datos para asignarle a la cuenta")
        return 0
    for i, row in enumerate(roles):
        print(str(row[0])+".- "+row[1])
    id_roles = iterarValidacion("Ingresa el numero que represente el rol de la cuenta\n")
    return id_roles
def Cuentas():
    cuentas = cuenta.leer_cuentas()
    if(cuentas == []):
        print("No existen cuentas en la base de datos para asignarle al empleado")
        return 0
    for i, row in enumerate(cuentas):
        print(str(row[0])+".- "+row[2])
    id_cuenta = iterarValidacion("Ingresa el numero que represente la cuenta a asignar\n")
    return id_cuenta

def crear_empleado(cuenta_id,rol_id,tienda_id,nombre, apellido_paterno, apellido_materno):
    valores = [cuenta_id,tienda_id,nombre, apellido_paterno,apellido_materno,1]
    if(rol_id == 2):
        resultado = empleado.crear_empleado_almacen(valores)
    elif(rol_id == 3 or rol_id == 1 ):
        resultado = empleado.crear_empleado_tienda(valores)
    if(resultado == True):
        showinfo(message="Se ha registrado con exito al empleado", title="Proceso exitoso")
    else:
        showerror(message="Ha ocurrido un error al registrar al empleado", title="Proceso fallido")
        
def mostrar_empleados():
    empleados = empleado.leer_empleados()
    print("ID\tCuenta\tAlmacen/Tienda\tNombre\tApellido Paterno\tApellido Materno\tFecha\n")
    for row in empleados:
        print(str(row[0])+"\t"+str(row[1])+"\t"+str(row[2])+"\t"+str(row[3])+"\t"+str(row[4])+"\t"+str(row[5])+"\t"+str(row[6]))

def editar_empleado(id,nombre,apellido_paterno,apellido_materno,lugar_trabajo_id):
    valor_viejo = empleado.leer_empleado(id)
    valores = [valor_viejo[1],valor_viejo[4],valor_viejo[5],valor_viejo[6]]
    valores[0]=lugar_trabajo_id
    valores[1]=nombre
    valores[2]=apellido_paterno
    valores[3]=apellido_materno
    resultado = empleado.editar_empleado_tienda(id,valores)
    if(resultado == True):
        showinfo(message="Se ha actualizado la informacion del empleado correctamente", title="Proceso exitoso")
    else:
        showerror(message="Ha ocurrido un error al actualizar la informacion", title="Proceso fallido")

def eliminar_empleado(id):
    confirmacion = askyesno("Confirmacion de eliminacion", "¿Estás seguro de que deseas eliminar al empleado?")
    if confirmacion:
        info_empleado = empleado.leer_empleado(id)
        resultado = cuenta.eliminar_cuenta(info_empleado[8])
        if(resultado == True):
            resultado2 = empleado.eliminar_empleado(id)
            if(resultado2 == True):
                showinfo(message="Se ha eliminado con exito al empleado", title="Proceso exitoso")
            else:
                showerror(message="Ha ocurrido un error al eliminar al empleado", title="Proceso fallido")
            showinfo(message="Se ha eliminado con exito la cuenta", title="Proceso exitoso")
        else:
            showerror(message="Ha ocurrido un error al eliminar la cuenta", title="Proceso fallido")
    else:
        showinfo(message="El proceso fue cancelado", title="Cancelar")
"""
opcion = 0
while(opcion!=5):
    print("MENU\n1.- Crear Empleado\n2.- Mostrar Empleados\n3.- Editar Empleado\n4.- Eliminar Empleado\n5.- Salir")
    opcion = validarOpcion("Ingresa el numero que  corresponda a la opcion deseada\n")
    if(opcion==1):
        crear_empleado()
    elif(opcion==2):
        mostrar_empleados()
    elif(opcion == 3):
        mostrar_empleados()
        id = iterarValidacion("Escribe el ID correspondiente del empleado a editar\n")
        editar_empleado(id)
    elif(opcion == 4):
        mostrar_empleados()
        id = iterarValidacion("Escribe el ID correspondiente del empleado a eliminar\n")
        eliminar_empleado(id)
    elif(opcion==5):
        print("Saliendo del programa...")
    else:
        opcion = 5
        print("Esa opcion no esta registrada. Saliendo del programa...")
        """