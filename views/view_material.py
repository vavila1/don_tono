import sys
import os
directorio_actual = os.getcwd()
directorio_models = os.path.dirname(directorio_actual)
directorio_models+= "/models"
sys.path.append(directorio_models)
import model_material as material
import model_tipo_unidad as tipo_unidad
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
def crear_material():
    print("crear_material")
    tipos = tipo_unidad.leer_tipos_unidades()
    for i, row in enumerate(tipos):
        print(str(row[0])+".- "+row[1])
    id_tipo_material = iterarValidacion("Ingresa el numero que represente como se va a identificar el material\n")


    preguntas = ["Escribe el nombre del material","Escribe el precio del material"]
    valores = []
    valores.append(id_tipo_material)
    for i in preguntas:
        valores.append(input(i+"\n"))
    valores.append(1)
    resultado = material.crear_material(valores)
    if(resultado == True):
        print("Se ha registrado con exito la tienda")
    else:
        print("Ha ocurrido un error al registrar la tienda")
def mostrar_materiales():
    almacenes = material.leer_materiales()
    print("ID\tNombre\tPrecio\tFecha\n")
    for row in almacenes:
        print(str(row[0])+"\t"+str(row[2])+"\t"+str(row[3])+"\t"+str(row[5]))
"""def editar_almacen(id):
    valor_viejo = almacen.leer_almacen(id)
    valores = [valor_viejo[1],valor_viejo[2]]
    inputs = []
    opcion1 = validarOpcion("Ingresa 1 en caso de querer editar el nombre\nIngresa 2 para pasar al siguiente dato\n")
    if(opcion1 == 1):
        nombre = input("Escribe el nombre nuevo\n")
        valores[0] = nombre
        inputs.append(1)
    else:
        inputs.append(2)
    opcion2 = validarOpcion("Ingresa 1 en caso de querer editar la direccion\nIngresa 2 para pasar al siguiente dato\n")
    if(opcion2 == 1):
        dir = input("Escribe la nueva direccion\n")
        valores[1] = dir
        inputs.append(1)
    else:
        inputs.append(2)
    if(inputs[0] == 1 or inputs[1] == 1):
        resultado = almacen.editar_almacen(id,valores)
        if(resultado == True):
            print("Se ha editado con exito la tienda")
        else:
            print("Ocurrio un error al editar la tienda")
    else:
        print("No hay nada que editar")
def eliminar_almacen(id):
    resultado = almacen.eliminar_almacen(id)
    if(resultado == True):
        print("Se ha eliminado la tienda con exito")
    else:
        print("Hubo un error al eliminar la tienda")"""
opcion = 0
while(opcion!=5):
    print("MENU\n1.- Crear Material\n2.- Mostrar Tiendas\n3.- Editar Tienda\n4.- Eliminar Tienda\n5.- Salir")
    opcion = validarOpcion("Ingresa el numero que  corresponda a la opcion deseada\n")
    if(opcion==1):
        crear_material()
    elif(opcion == 2):
        mostrar_materiales()
    elif(opcion==5):
        print("Saliendo del programa...")
    else:
        print("Esa opcion no esta registrada. Saliendo del programa...")
