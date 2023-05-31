import sys
import os
directorio_actual = os.getcwd()
directorio_models = os.path.dirname(directorio_actual)
directorio_models+= "/models"
sys.path.append(directorio_models)
import model_empleado as empleado
import model_cuenta as cuenta
import model_almacen as almacen
import model_tienda as tienda
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
def crear_empleado():
    id_rol = Roles()
    if(id_rol == 0):
        return
    preguntas_cuenta = ["Escribe el correo de la cuenta","Escribe la contrasena de la cuenta"]
    valores_cuenta = []
    valores_cuenta.append(id_rol)
    for i in preguntas_cuenta:
        valores_cuenta.append(input(i+"\n"))
    valores_cuenta.append(1)
    """------------------------------------------------------------------------------------------"""
    
    preguntas = ["Escribe el nombre del empleado","Escribe el apellido paterno del empleado","Escribe el apellido materno del empleado"]
    valores = []
    opcion1 = iterarValidacion("Ingresa 1 si deseas que el empleado se asigne a un almacen\nIngresa 2 si deseas que el empleado se asigne a una tienda\n")
    if(opcion1 == 1):
        id_almacen = Almacenes()
        if(id_almacen == 0):
            return
        resultado = cuenta.crear_cuenta(valores_cuenta)
        if(resultado == True):
            print("Se ha registrado con exito la cuenta")
        else:
            print("Ha ocurrido un error al registrar la cuenta")
            return
        id_cuenta = cuenta.leer_cuenta_correo(valores_cuenta[1])
        id_cuenta = id_cuenta[0]
        valores.append(id_cuenta)
        valores.append(id_almacen)
        for i in preguntas:
            valores.append(input(i+"\n"))
        valores.append(1)
        resultado = empleado.crear_empleado_almacen(valores)
    elif(opcion1 == 2):
        id_tienda = Tiendas()
        if(id_tienda == 0):
            return
        resultado = cuenta.crear_cuenta(valores_cuenta)
        if(resultado == True):
            print("Se ha registrado con exito la cuenta")
        else:
            print("Ha ocurrido un error al registrar la cuenta")
            return
        id_cuenta = cuenta.leer_cuenta_correo(valores_cuenta[1])
        id_cuenta = id_cuenta[0]
        valores.append(id_cuenta)
        valores.append(id_tienda)
        for i in preguntas:
            valores.append(input(i+"\n"))
        valores.append(1)
        resultado = empleado.crear_empleado_tienda(valores)
    if(resultado == True):
        print("Se ha registrado con exito el empleado")
    else:
        print("Ha ocurrido un error al registrar el empleado")
def mostrar_empleados():
    empleados = empleado.leer_empleados()
    print("ID\tCuenta\tAlmacen/Tienda\tNombre\tApellido Paterno\tApellido Materno\tFecha\n")
    for row in empleados:
        print(str(row[0])+"\t"+str(row[1])+"\t"+str(row[2])+"\t"+str(row[3])+"\t"+str(row[4])+"\t"+str(row[5])+"\t"+str(row[6]))
def editar_empleado(id):
    valor_viejo = empleado.leer_empleado(id)
    if(valor_viejo == []):
        print("No existe el dato en la base de datos")
        return
    valores = [valor_viejo[1],valor_viejo[4],valor_viejo[5],valor_viejo[6]]
    inputs = []
    lugar_trabajo = 0
    opcion1 = iterarValidacion("Ingresa 1 en caso de querer editar el lugar de trabajo \nIngresa 2 para pasar al siguiente dato\n")
    if(opcion1 == 1):
        opcion2 = iterarValidacion("Ingresa 1 si deseas que el empleado se asigne a un almacen\nIngresa 2 si deseas que el empleado se asigne a una tienda\n")
        if(opcion2==1):
            id_almacen = Almacenes()
            valores[0] = id_almacen
            inputs.append(1)
            lugar_trabajo = 1
        elif(opcion2 == 2):
            id_tienda = Tiendas()
            valores[0] = id_tienda
            inputs.append(1)
            lugar_trabajo = 2
    else:
        inputs.append(2)
    opcion3 = iterarValidacion("Ingresa 1 en caso de querer editar el nombre del empleado \nIngresa 2 para pasar al siguiente dato\n")
    if(opcion3 == 1):
        nombre = input("Escribe el nuevo nombre del empleado\n")
        valores[1] = nombre
        inputs.append(1)
    else:
        inputs.append(2)
    opcion4 = iterarValidacion("Ingresa 1 en caso de querer editar el apellido paterno del empleado\nIngresa 2 para pasar al siguiente dato\n")
    if(opcion4 == 1):
        apellido_paterno = input("Escribe el nuevo apellido paterno\n")
        valores[2] = apellido_paterno
        inputs.append(1)
    else:
        inputs.append(2)
    opcion5 = iterarValidacion("Ingresa 1 en caso de querer editar el apellido materno del empleado\nIngresa 2 para pasar al siguiente dato\n")
    if(opcion5 == 1):
        apellido_materno = input("Escribe el nuevo apellido materno\n")
        valores[3] = apellido_materno
        inputs.append(1)
    else:
        inputs.append(2)
    if(inputs[0] == 1 or inputs[1] == 1 or inputs[2] == 1 or inputs[3] == 1):
        if(lugar_trabajo == 1 or lugar_trabajo == 0):
            resultado = empleado.editar_empleado_almacen(id,valores)
            if(resultado == True):
                print("Se ha editado con exito al empleado")
            else:
                print("Ocurrio un error al editar el empleado")
        elif(lugar_trabajo == 2 or lugar_trabajo == 0):
            resultado = empleado.editar_empleado_tienda(id,valores)
            if(resultado == True):
                print("Se ha editado con exito la cuenta")
            else:
                print("Ocurrio un error al editar la cuenta")
    else:
        print("No hay nada que editar")
def eliminar_empleado(id):
    info_empleado = empleado.leer_empleado(id)
    if(info_empleado == []):
        print("No existe en la base de datos")
        return
    resultado = cuenta.eliminar_cuenta(info_empleado[8])
    if(resultado == True):
        print("Se ha eliminado la cuenta con exito")
        resultado2 = empleado.eliminar_empleado(id)
        if(resultado2 == True):
            print("Se ha eliminado el empleado con exito")
        else:
            print("Hubo un error al eliminar el empleado")
    else:
        print("Hubo un error al eliminar cuenta")
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