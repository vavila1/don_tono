import sys
import os
directorio_actual = os.getcwd()
directorio_models = os.path.dirname(directorio_actual)
directorio_models+= "/models"
sys.path.append(directorio_models)
import model_rol as rol
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
def crear_rol():
    preguntas = ["Escribe el nombre del rol"]
    valores = []
    for i in preguntas:
        valores.append(input(i+"\n"))
    valores.append(1)
    resultado = rol.crear_rol(valores)
    if(resultado == True):
        print("Se ha registrado con exito el rol")
    else:
        print("Ha ocurrido un error al registrar el rol")
def mostrar_roles():
    roles = rol.leer_roles()
    print("ID\tNombre\tFecha\n")
    for row in roles:
        print(str(row[0])+"\t"+str(row[1])+"\t"+str(row[3]))
def editar_rol(id):
    valor_viejo = rol.leer_rol(id)
    if(valor_viejo == []):
        print("No existe el dato en la base de datos")
        return
    valores = [valor_viejo[1]]
    inputs = []
    opcion1 = iterarValidacion("Ingresa 1 en caso de querer editar el nombre del rol \nIngresa 2 para pasar al siguiente dato\n")
    if(opcion1 == 1):
        nombre = input("Escribe el nuevo nombre\n")
        valores[0] = nombre
        inputs.append(1)
    else:
        inputs.append(2)

    if(inputs[0] == 1):
        resultado = rol.editar_rol(id,valores)
        if(resultado == True):
            print("Se ha editado con exito el rol")
        else:
            print("Ocurrio un error al editar el rol")
    else:
        print("No hay nada que editar")
def eliminar_rol(id):
    resultado = rol.leer_rol(id)
    if(resultado == []):
        print("No existe en la base de datos")
        return
    resultado = rol.eliminar_rol(id)
    if(resultado == True):
        print("Se ha eliminado el material con exito")
    else:
        print("Hubo un error al eliminar la tienda")
opcion = 0
while(opcion!=5):
    print("MENU\n1.- Crear Rol\n2.- Mostrar Roles\n3.- Editar Rol\n4.- Eliminar Rol\n5.- Salir")
    opcion = validarOpcion("Ingresa el numero que  corresponda a la opcion deseada\n")
    if(opcion==1):
        crear_rol()
    elif(opcion==2):
        mostrar_roles()
    elif(opcion == 3):
        mostrar_roles()
        id = iterarValidacion("Escribe el ID correspondiente del rol a editar\n")
        editar_rol(id)
    elif(opcion == 4):
        mostrar_roles()
        id = iterarValidacion("Escribe el ID correspondiente del rol a eliminar\n")
        eliminar_rol(id)
    elif(opcion==5):
        print("Saliendo del programa...")
    else:
        opcion = 5
        print("Esa opcion no esta registrada. Saliendo del programa...")