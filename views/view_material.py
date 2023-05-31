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
def tiposUnidad():
    tipos = tipo_unidad.leer_tipos_unidades()
    for i, row in enumerate(tipos):
        print(str(row[0])+".- "+row[1])
    id_tipo_material = iterarValidacion("Ingresa el numero que represente como se va a identificar el material\n")
    return id_tipo_material
def crear_material():
    id_tipo_material = tiposUnidad()

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
    materiales = material.leer_materiales()
    print("ID\tNombre\tPrecio\tTipo de Unidad\tFecha\n")
    for row in materiales:
        unidad = tipo_unidad.leer_tipo_unidad(row[1])
        print(str(row[0])+"\t"+str(row[2])+"\t"+str(row[3])+"\t"+str(unidad[1])+"\t"+str(row[5]))
def editar_material(id):
    valor_viejo = material.leer_material(id)
    if(valor_viejo == []):
        print("No existe el dato en la base de datos")
        return
    valores = [valor_viejo[1],valor_viejo[2],valor_viejo[3]]
    inputs = []
    opcion1 = iterarValidacion("Ingresa 1 en caso de querer editar el tipo de unidad del material\nIngresa 2 para pasar al siguiente dato\n")
    if(opcion1 == 1):
        id_tipo_material = tiposUnidad()
        valores[0] = id_tipo_material
        inputs.append(1)
    else:
        inputs.append(2)
    opcion2 = iterarValidacion("Ingresa 1 en caso de querer editar el nombre del material\nIngresa 2 para pasar al siguiente dato\n")
    if(opcion2 == 1):
        nombre = input("Escribe la nueva direccion\n")
        valores[1] = nombre
        inputs.append(1)
    else:
        inputs.append(2)
    opcion3 = iterarValidacion("Ingresa 1 en caso de querer editar el precio del material\nIngresa 2 para pasar al siguiente dato\n")
    if(opcion3 == 1):
        precio = iterarValidacion("Escribe el nuevo precio\n")
        valores[2] = precio
        inputs.append(1)
    else:
        inputs.append(2)

    if(inputs[0] == 1 or inputs[1] == 1 or inputs[2] == 1):
        resultado = material.editar_material(id,valores)
        if(resultado == True):
            print("Se ha editado con exito la tienda")
        else:
            print("Ocurrio un error al editar la tienda")
    else:
        print("No hay nada que editar")
def eliminar_material(id):
    resultado = material.leer_material(id)
    if(resultado == []):
        print("No existe en la base de datos")
        return
    resultado = material.eliminar_material(id)
    if(resultado == True):
        print("Se ha eliminado el material con exito")
    else:
        print("Hubo un error al eliminar la tienda")
opcion = 0
while(opcion!=5):
    print("MENU\n1.- Crear Material\n2.- Mostrar Materiales\n3.- Editar Material\n4.- Eliminar Material\n5.- Salir")
    opcion = validarOpcion("Ingresa el numero que  corresponda a la opcion deseada\n")
    if(opcion==1):
        crear_material()
    elif(opcion == 2):
        mostrar_materiales()
    elif(opcion == 3):
        mostrar_materiales()
        id = iterarValidacion("Escribe el ID correspondiente del material a editar\n")
        editar_material(id)
    elif(opcion == 4):
        mostrar_materiales()
        id = iterarValidacion("Escribe el ID correspondiente del material a eliminar\n")
        eliminar_material(id)
    elif(opcion==5):
        print("Saliendo del programa...")
    else:
        opcion = 5
        print("Esa opcion no esta registrada. Saliendo del programa...")
