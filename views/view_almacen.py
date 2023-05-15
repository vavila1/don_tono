from models import model_almacen
import model_almacen as alm 

def pedir_datos_almacen():
    nombre = input("Ingresa el nombre del almacen")
    direccion = input("Ingrese la dirección del almacen: ")
    estatus = 1  # Por defecto, el estatus será activo (1)
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
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            valores = pedir_datos_almacen()
            if alm.crear_almacen(valores):
                print("¡Almacen creado exitosamente!")
            else:
                print("Error al crear el almacen.")

        elif opcion == 2:
            resultados = alm.leer_almacenes()
            print("\n----- Almacenes -----")
            for resultado in resultados:
                print(resultado)

        elif opcion == 3:
            id = input("Ingrese el ID del almacen a buscar: ")
            resultado = alm.leer_almacen(id)
            if resultado:
                print("\n----- Almacen encontrado -----")
                print(resultado)
            else:
                print("No se encontró ningún almacen con ese ID.")

        elif opcion == 4:
            id = input("Ingrese el ID del almacen a editar: ")
            valores = pedir_datos_almacen()
            valores.append(alm.timestamp())
            if alm.editar_almacen(id, valores):
                print("¡Almacen editado exitosamente!")
            else:
                print("Error al editar el almacen.")

        elif opcion == 5:
            id = input("Ingrese el ID del almacen a eliminar: ")
            if alm.eliminar_almacen(id):
                print("¡Almacen eliminado exitosamente!")
            else:
                print("Error al eliminar el almacen.")

        elif opcion == 6:
            print("¡Hasta luego, gracias por usar el sistema Don Toño!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")
