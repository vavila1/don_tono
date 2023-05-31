#Aqui se encuentra CRUD tipo_operacion
import funciones_model as q

def crear_tipo_operacion(valores):
    valores.append(q.timestamp())
    resultado = q.mod("INSERT INTO tipo_de_operacion (nombre, estatus, created_at) VALUES (%s, %s, %s)",
                  (valores[0], valores[1],valores[2]))
    return resultado
def leer_tipo_operaciones():
    resultado = q.select('Select * from tipo_de_operacion where estatus = 1')
    resultado = q.consulta_lista(resultado)
    return resultado
def leer_tipo_operacion(id):
    consulta = "Select * from tipo_de_operacion where id = "+str(id)+" AND estatus = 1"
    resultado = q.select(consulta)
    resultado = q.consulta_lista(resultado)
    if(resultado != []):
        return resultado[0]
    return resultado
def editar_tipo_operacion(id,valores):
    #esto sirve para agregar el id al final de la lista ya que asi es la sintaxis para agregar valores a la consulta
    valores.append(q.timestamp())
    valores.append(id)
    resultado = q.mod("Update tipo_de_operacion set nombre = %s, updated_at = %s where id = %s",(valores[0],valores[1],valores[2]))
    return resultado
def eliminar_tipo_operacion(id):
    resultado = q.mod("Update tipo_de_operacion set estatus = %s where id = %s",(2,id))
    return resultado