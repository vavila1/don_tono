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