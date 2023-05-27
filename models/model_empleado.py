#Aqui se encuentra CRUD empleado
import funciones_model as q

def crear_empleado_almacen(valores):
    valores.append(q.timestamp())
    resultado = q.mod("INSERT INTO empleado (cuenta_id, almacen_id, nombre, apellido_paterno, apellido_materno, estatus, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                  (valores[0], valores[1],valores[2],valores[3],valores[4],valores[5],valores[6]))
    return resultado
def crear_empleado_tienda(valores):
    valores.append(q.timestamp())
    resultado = q.mod("INSERT INTO empleado (cuenta_id, tienda_id, nombre, apellido_paterno, apellido_materno, estatus, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                  (valores[0], valores[1],valores[2],valores[3],valores[4],valores[5],valores[6]))
    return resultado
def leer_empleados():
    resultado = q.select("SELECT empleado.id AS id, cuenta.correo AS cuenta, COALESCE(tienda.nombre, almacen.nombre) AS trabajo, empleado.nombre AS nombre, empleado.apellido_paterno AS apellido_paterno, empleado.apellido_materno AS apellido_materno, empleado.created_at AS created_at FROM empleado JOIN cuenta ON empleado.cuenta_id = cuenta.id LEFT JOIN tienda ON empleado.tienda_id = tienda.id LEFT JOIN almacen ON empleado.almacen_id = almacen.id WHERE empleado.estatus = 1")
    resultado = q.consulta_lista(resultado)
    return resultado
def leer_cuenta(id):
    consulta = "Select cuenta.id as id, rol.nombre as rol, rol.id as id_rol, cuenta.correo, cuenta.contra, cuenta.created_at from rol,cuenta where cuenta.id = "+str(id)+" AND cuenta.estatus = 1 AND cuenta.rol_id = rol.id"
    resultado = q.select(consulta)
    resultado = q.consulta_lista(resultado)
    if(resultado != []):
        return resultado[0]
    return resultado
def editar_cuenta(id,valores):
    #esto sirve para agregar el id al final de la lista ya que asi es la sintaxis para agregar valores a la consulta
    valores.append(q.timestamp())
    valores.append(id)
    resultado = q.mod("Update cuenta set rol_id = %s, correo = %s, contra = %s, updated_at = %s where id = %s",(valores[0],valores[1],valores[2],valores[3],valores[4]))
    return resultado
def eliminar_cuenta(id):
    resultado = q.mod("Update cuenta set estatus = %s where id = %s",(2,id))
    return resultado