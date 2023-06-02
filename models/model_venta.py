import funciones_model as q

def registrar_venta(valores):
    valores.append(q.timestamp())
    resultado = q.mod("INSERT into venta (empleado_id,  tienda_id, created_at) VALUES (%s, %s, %s)", (valores[0], valores[1], valores[2]))
    return resultado

def editar_venta(id, valores):
    valores.append(q.timestamp())
    valores.append(id)
    resultado = q.mod("UPDATE venta SET empleado_id = %s, tienda_id = %s, updated_at = %s WHERE id = %s", (valores[0], valores[1], valores[2], valores[4]))
    return resultado


def eliminar_venta(id):
    resultado = q.mod("DELETE FROM venta WHERE id = %s", (id))
    return resultado

def existencia_material(valores):
    consulta = "SELECT cantidad from existencias_tienda where existencias_tienda.tienda_id = "+str(valores[1])+" AND existencias_tienda.tienda_id = "+str(valores[2])
    resultado = q.select(consulta)
    resultado = q.consulta_lista(resultado)
    if(resultado != []):
        return resultado[0][0]
    return resultado
def ultima_venta_id():
    consulta = "Select id from ventas ORDER BY id DESC limit 1"
    resultado = q.select(consulta)
    resultado = q.consulta_lista(resultado)
    if(resultado != []):
        return resultado[0][0]
    return resultado
def existencia_id(valores):
    consulta = "Select id from existencias_tienda where existencias_tienda.tienda_id = "+str(valores[1])+" AND existencias_tienda.material_id = "+str(valores[2])
    resultado = q.select(consulta)
    resultado = q.consulta_lista(resultado)
    if(resultado != []):
        return resultado[0][0]
    return resultado
def existencias_tienda(tienda_id):
    consulta = "Select material.id, material.nombre,cantidad from material, existencias_tienda where existencias_tienda.tienda_id = "+str(tienda_id)+" AND existencias_tienda.material_id = material.id"
    resultado = q.select(consulta)
    resultado = q.consulta_lista(resultado)
    return resultado
def precio_material(material_id):
    consulta = "Select precio from material where material.id = "+str(material_id)
    resultado = q.select(consulta)
    resultado = q.consulta_lista(resultado)
    if(resultado != []):
        return resultado[0][0]
    return resultado
def registrar_venta(valores,venta_id):
    try:
        # Iniciar la transacción
        conexion = q.conexion()
        precio = precio_material(valores[1])
        precio = precio*valores[3]
        cursor = conexion.cursor()
        valores.append(1)
        valores.append(q.timestamp())
        cantidad_actual = existencia_material(valores)
        cantidad_nueva = cantidad_actual - valores[3]
        var_existencia_id = existencia_id(valores)
        print(valores)
        # Verificar si hay suficientes existencias del producto en la tienda
        if cantidad_actual >= valores[3]:
            # Realizar la venta
            cursor.execute("Insert into ventas (id, tienda_id, material_id, empleado_id, cantidad, precio, estatus, created_at) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(venta_id,valores[0],valores[1],valores[2],valores[3],precio,valores[4],valores[5]))
            cursor.execute("UPDATE existencias_tienda SET cantidad = %s, updated_at = %s WHERE id = %s",(cantidad_nueva,q.timestamp(),var_existencia_id))

            # Confirmar la transacción
            conexion.commit()
            print("Venta realizada con éxito")
            return True
        else:
            print("No hay suficientes existencias del producto en la tienda")

    except Exception as error:
        # Ocurrió un error, deshacer la transacción
        conexion.rollback()
        print("Error durante la transacción:", error)
        return False

    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        conexion.close()