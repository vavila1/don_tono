import sys
import os
directorio_actual = os.getcwd()
directorio_models = os.path.dirname(directorio_actual)
directorio_models+= "/models"
sys.path.append(directorio_models)
import model_tipo_unidad as tipo_unidad
def validarOpcion(mensaje):
  try:
    variable = int(input(mensaje))
    return variable
  except:
    print("Debes ingresar un numero que corresponda a la opción elegida")
    return False
def crear_tipo_unidad():
    preguntas = ["Escribe el nombre del tipo de unidad"]
    valores = []
    for i in preguntas:
        valores.append(input(i+"\n"))
    valores.append(1)
    resultado = tipo_unidad.crear_tipo_unidad(valores)
    if(resultado == True):
        print("Se ha registrado con exito la tienda")
    else:
        print("Ha ocurrido un error al registrar la tienda")
def mostrar_tipo_unidad():
    tiendas = tipo_unidad.leer_tipos_unidades()
    print("ID\tNombre\tFecha\n")
    for row in tiendas:
        print(str(row[0])+"\t"+str(row[1])+"\t"+str(row[3]))
def editar_tipo_unidad(id):
    valor_viejo = tipo_unidad.leer_tipo_unidad(id)
    valores = [valor_viejo[1]]
    inputs = []
    opcion1 = validarOpcion("Ingresa 1 en caso de querer editar el nombre\nIngresa 2 para pasar al siguiente dato\n")
    if(opcion1 == 1):
        nombre = input("Escribe el nombre nuevo\n")
        valores[0] = nombre
        inputs.append(1)
    else:
        inputs.append(2)
    if(inputs[0] == 1):
        resultado = tipo_unidad.editar_tipo_unidad(id,valores)
        if(resultado == True):
            print("Se ha editado con exito la tienda")
        else:
            print("Ocurrio un error al editar la tienda")
    else:
        print("No hay nada que editar")
def eliminar_tipo_unidad(id):
    resultado = tipo_unidad.eliminar_tipo_unidad(id)
    if(resultado == True):
        print("Se ha eliminado la tienda con exito")
    else:
        print("Hubo un error al eliminar la tienda")
opcion = 0
while(opcion!=5):
    print("MENU\n1.- Crear Tipo de Unidad\n2.- Mostrar Tipo de Unidades\n3.- Editar Tipo de Unidades\n4.- Eliminar Tipo de Unidad\n5.- Salir")
    opcion = validarOpcion("Ingresa el numero que  corresponda a la opcion deseada\n")
    if(opcion==1):
        crear_tipo_unidad()
    elif(opcion==2):
        mostrar_tipo_unidad()
    elif(opcion==3):
        mostrar_tipo_unidad()
        id = validarOpcion("Escribe el ID correspondiente del tipo de unidad a editar\n")
        editar_tipo_unidad(id)
    elif(opcion == 4):
        mostrar_tipo_unidad()
        id = validarOpcion("Escribe el ID correspondiente del tipo de unidad a eliminar\n")
        eliminar_tipo_unidad(id)
    elif(opcion==5):
        print("Saliendo del programa...")
    else:
        print("Esa opcion no esta registrada. Saliendo del programa...")