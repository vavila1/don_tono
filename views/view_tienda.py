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
opcion = 0
while(opcion!=2):
    print("MENU\n1- Crear Tienda\n2.-Salir")
    opcion = validarOpcion("Ingresa el numero que  corresponda a la opcion deseada\n")
    if(opcion==1):
        crear_tienda()
    elif(opcion==2):
        print("Saliendo del programa...")
    else:
        print("Esa opcion no esta registrada. Saliendo del programa...")