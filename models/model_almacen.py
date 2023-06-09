#Aqui se encuentra el CRUD de almacenes
import funciones_model as q

def crear_almacen(valores):
    valores.append(q.timestamp())
    resultado = q.mod("INSERT INTO almacen (nombre, direccion, estatus, created_at) VALUES (%s, %s, %s,%s)",
                  (valores[0], valores[1], valores[2],valores[3]))
    return resultado
def leer_almacenes():
    resultado = q.select('Select * from almacen where estatus = 1')
    resultado = q.consulta_lista(resultado)
    return resultado
def leer_almacen(id):
    resultado = q.select("Select * from almacen where id ="+str(id)+"AND status=1")
    resultado = q.consulta_lista(resultado)
    return resultado[0]
def editar_almacen(id,valores):
    #esto sirve para agregar el id al final de la lista ya que asi es la sintaxis para agregar valores a la consulta
    valores.append(id)
    resultado = q.mod("Update almacen set nombre = %s, direccion = %s, updated_at = %s where id = %s",(valores[0],valores[1],valores[2],valores[3]))
    return resultado
def eliminar_almacen(id):
    resultado = q.mod("Update almacen set estatus = %s where id = %s",(2,id))
    return resultado