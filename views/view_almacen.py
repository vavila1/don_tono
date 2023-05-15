from models import model_almacen
import model_almacen as alm 

def pedir_datos_almacen():
    nombre = input("Ingresa el nombre del almacen")
    direccion = input("Ingrese la dirección del almacen: ")
    estatus = 1  # Por defecto, el estatus será activo
    return [nombre, direccion, estatus]

def menu_almacenes():
    while True:
        print("\n----- Menú de Almacenes -----")
        print("1. Crear Almacen")
        print("2. Leer Almacenes")
        print("3. Leer Almacen por ID")
        print("4. Editar Almacen")
        print("5. Eliminar Almacen")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")