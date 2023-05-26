import sys
import os
directorio_actual = os.getcwd()
directorio_models = os.path.dirname(directorio_actual)
directorio_models+= "/models"
sys.path.append(directorio_models)
import model_tipo_operacion as tipo_operacion
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
    preguntas = ["Escribe el nombre de la operacion"]
    valores = []
    for i in preguntas:
        valores.append(input(i+"\n"))
    valores.append(1)
    resultado = tipo_operacion.crear_tipo_operacion(valores)
    if(resultado == True):
        print("Se ha registrado con exito la tienda")
    else:
        print("Ha ocurrido un error al registrar la tienda")
def mostrar_tipo_operacion():
    tipo_operaciones = tipo_operacion.leer_tipo_operaciones()
    print("ID\tNombre\tFecha\n")
    for row in tipo_operaciones:
        print(str(row[0])+"\t"+str(row[1])+"\t"+str(row[3]))
def editar_tipo_operacion(id):
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
        print("No hay nada que editar")
def eliminar_tipo_operacion(id):
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
        print("Esa opcion no esta registrada. Saliendo del programa...")