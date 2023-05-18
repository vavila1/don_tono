import sys
sys.path.append("/Users/victoravila/Desktop/Tecnologías de información emergentes/Proyecto Final/don_tono/models")
import model_tienda as tienda
def validarOpcion(mensaje):
  try:
    variable = int(input(mensaje))
    return variable
  except:
    print("Debes ingresar un numero que corresponda a la opción elegida")
    return False
def crear_tienda():
    preguntas = ["Escribe el nombre de la tienda","Escribe la direccion de la tienda"]
    valores = []
    for i in preguntas:
        valores.append(input(i+"\n"))
    valores.append(1)
    resultado = tienda.crear_tienda(valores)
    if(resultado == True):
        print("Se ha registrado con exito la tienda")
    else:
        print("Ha ocurrido un error al registrar la tienda")
def mostrar_tiendas():
    tiendas = tienda.leer_tiendas()
    print("ID\tNombre\tDireccion\tFecha\n")
    for row in tiendas:
        print(str(row[0])+"\t"+str(row[1])+"\t"+str(row[2])+"\t"+str(row[4]))
def editar_tienda(id):
    valor_viejo = tienda.leer_tienda(id)
    valores = [valor_viejo[1],valor_viejo[2]]
    inputs = []
    opcion1 = validarOpcion("Ingresa 1 en caso de querer editar el nombre\nIngresa 2 para pasar al siguiente dato\n")
    if(opcion1 == 1):
        nombre = input("Escribe el nombre nuevo")
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
        resultado = tienda.editar_tienda(id,valores)
        if(resultado == True):
            print("Se ha editado con exito la tienda")
        else:
            print("Ocurrio un error al editar la tienda")
    else:
        print("No hay nada que editar")
def eliminar_tienda(id):
    resultado = tienda.eliminar_tienda(id)
    if(resultado == True):
        print("Se ha eliminado la tienda con exito")
    else:
        print("Hubo un error al eliminar la tienda")    

opcion = 0
while(opcion!=5):
    print("MENU\n1.- Crear Tienda\n2.- Mostrar Tiendas\n3.- Editar Tienda\n4.- Eliminar Tienda\n5.- Salir")
    opcion = validarOpcion("Ingresa el numero que  corresponda a la opcion deseada\n")
    if(opcion==1):
        crear_tienda()
    elif(opcion == 2):
        mostrar_tiendas()
    elif(opcion == 3):
        mostrar_tiendas()
        id = validarOpcion("Escribe el ID correspondiente de la tienda a editar\n")
        editar_tienda(id)
    elif(opcion == 4):
        mostrar_tiendas()
        id = validarOpcion("Escribe el ID correspondiente de la tienda a eliminar\n")
        eliminar_tienda(id)
    elif(opcion==5):
        print("Saliendo del programa...")
    else:
        print("Esa opcion no esta registrada. Saliendo del programa...")