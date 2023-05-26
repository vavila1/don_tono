import sys
import os
directorio_actual = os.getcwd()
directorio_models = os.path.dirname(directorio_actual)
directorio_models+= "/models"
sys.path.append(directorio_models)
import model_rol as rol
import model_cuenta as cuenta
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
def Roles():
    roles = rol.leer_roles()
    if(roles == []):
        print("No existen roles en la base de datos para asignarle a la cuenta")
        return 0
    for i, row in enumerate(roles):
        print(str(row[0])+".- "+row[1])
    id_roles = iterarValidacion("Ingresa el numero que represente el rol de la cuenta\n")
    return id_roles
def crear_cuenta():
    id_rol = Roles()
    if(id_rol == 0):
        return
    preguntas = ["Escribe el correo de la cuenta","Escribe la contrasena de la cuenta"]
    valores = []
    valores.append(id_rol)
    for i in preguntas:
        valores.append(input(i+"\n"))
    valores.append(1)
    resultado = cuenta.crear_cuenta(valores)
    if(resultado == True):
        print("Se ha registrado con exito el rol")
    else:
        print("Ha ocurrido un error al registrar el rol")
def mostrar_cuentas():
    cuentas = cuenta.leer_cuentas()
    print("ID\tRol\tCorreo\tFecha\n")
    for row in cuentas:
        print(str(row[0])+"\t"+str(row[1])+"\t"+str(row[2])+"\t"+str(row[4]))
def editar_cuenta(id):
    valor_viejo = cuenta.leer_cuenta(id)
    if(valor_viejo == []):
        print("No existe el dato en la base de datos")
        return
    valores = [valor_viejo[2],valor_viejo[3],valor_viejo[4]]
    inputs = []
    opcion1 = iterarValidacion("Ingresa 1 en caso de querer editar el rol de la cuenta \nIngresa 2 para pasar al siguiente dato\n")
    if(opcion1 == 1):
        rol = Roles()
        valores[0] = rol
        inputs.append(1)
    else:
        inputs.append(2)
    opcion2 = iterarValidacion("Ingresa 1 en caso de querer editar el correo de la cuenta \nIngresa 2 para pasar al siguiente dato\n")
    if(opcion2 == 1):
        correo = input("Escribe el nuevo correo\n")
        valores[1] = correo
        inputs.append(1)
    else:
        inputs.append(2)
    opcion3 = iterarValidacion("Ingresa 1 en caso de querer editar la contrasena de la cuenta\nIngresa 2 para pasar al siguiente dato\n")
    if(opcion3 == 1):
        contra = input("Escribe la nueva contrasena\n")
        valores[2] = contra
        inputs.append(1)
    else:
        inputs.append(2)
    if(inputs[0] == 1 or inputs[1] == 1 or inputs[2] == 1):
        resultado = cuenta.editar_cuenta(id,valores)
        if(resultado == True):
            print("Se ha editado con exito la cuenta")
        else:
            print("Ocurrio un error al editar la cuenta")
    else:
        print("No hay nada que editar")
def eliminar_cuenta(id):
    resultado = cuenta.leer_cuenta(id)
    if(resultado == []):
        print("No existe en la base de datos")
        return
    resultado = cuenta.eliminar_cuenta(id)
    if(resultado == True):
        print("Se ha eliminado el material con exito")
    else:
        print("Hubo un error al eliminar la tienda")
opcion = 0
while(opcion!=5):
    print("MENU\n1.- Crear Cuenta\n2.- Mostrar Cuentas\n3.- Editar Cuenta\n4.- Eliminar Cuenta\n5.- Salir")
    opcion = validarOpcion("Ingresa el numero que  corresponda a la opcion deseada\n")
    if(opcion==1):
        crear_cuenta()
    elif(opcion == 2):
        mostrar_cuentas()
    elif(opcion == 3):
        mostrar_cuentas()
        id = iterarValidacion("Escribe el ID correspondiente de la cuenta a editar\n")
        editar_cuenta(id)
    elif(opcion == 4):
        mostrar_cuentas()
        id = iterarValidacion("Escribe el ID correspondiente de la cuenta a eliminar\n")
        eliminar_cuenta(id)
    elif(opcion==5):
        print("Saliendo del programa...")
    else:
        opcion = 5
        print("Esa opcion no esta registrada. Saliendo del programa...")