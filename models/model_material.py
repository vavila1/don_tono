#Aqui se encuentra CRUD material
import funciones_model as q

def crear_material(valores):
    valores.append(q.timestamp())
    resultado = q.mod("INSERT INTO material (tipo_unidad_id, nombre, precio, estatus, created_at) VALUES (%s, %s, %s, %s, %s)",
                  (valores[0], valores[1],valores[2],valores[3],valores[4]))
    return resultado
def leer_materiales():
    resultado = q.select('Select * from material where estatus = 1')
    resultado = q.consulta_lista(resultado)
    return resultado
def leer_tipo_unidad(id):
    consulta = "Select * from tipo_unidad where id = "+str(id)
    resultado = q.select(consulta)
    resultado = q.consulta_lista(resultado)
    return resultado[0]
def editar_tipo_unidad(id,valores):
    #esto sirve para agregar el id al final de la lista ya que asi es la sintaxis para agregar valores a la consulta
    valores.append(q.timestamp())
    valores.append(id)
    resultado = q.mod("Update tipo_unidad set nombre = %s, updated_at = %s where id = %s",(valores[0],valores[1],valores[2]))
    return resultado
def eliminar_tipo_unidad(id):
    resultado = q.mod("Update tipo_unidad set estatus = %s where id = %s",(2,id))
    return resultado