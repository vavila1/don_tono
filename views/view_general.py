import sys
import os
directorio_actual = os.getcwd()
directorio_models = os.path.dirname(directorio_actual)
directorio_models+= "/models"
sys.path.append(directorio_models)
import model_sesion as sesion
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
def menu(info_cuenta):
    menu_opciones = []
    opciones = ["Operaciones Almacen","Operaciones Tienda"]
    print(info_cuenta)
    for i, pregunta in enumerate(opciones):
        if(info_cuenta[0] == 1 or info_cuenta[0] == 2):
            if(i!=1):
                print("Almacen")
        if(info_cuenta[0] == 1 or info_cuenta[0] == 3):
            if(i!=0):
                print("Tienda")
    opcion = 0
    while(opcion!=5):
        print("MENU\n")
        print(menu_opciones)
        opcion = validarOpcion("Ingresa el numero que  corresponda a la opcion deseada\n")
        if(opcion==1):
            print("Hola")
        elif(opcion==5):
            print("Saliendo del programa...")
        else:
            opcion = 5
            print("Esa opcion no esta registrada. Saliendo del programa...")
valores = []
preguntas = ["Ingresa tu correo\n","Ingresa la contrasena\n"]
for i in preguntas:
    valores.append(input(i))
resultado = sesion.verificar_contrasena(valores)
print(resultado)
if(resultado == True):
    info_cuenta = sesion.info_cuenta(valores)
    menu(info_cuenta)
else:
    print("Usuario y/o contraseña incorrectos")