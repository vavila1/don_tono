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
def leer_material(id):
    consulta = "Select * from material where id = "+str(id)+" AND estatus = 1"
    resultado = q.select(consulta)
    resultado = q.consulta_lista(resultado)
    if(resultado != []):
        return resultado[0]
    return resultado
def editar_material(id,valores):
    #esto sirve para agregar el id al final de la lista ya que asi es la sintaxis para agregar valores a la consulta
    valores.append(q.timestamp())
    valores.append(id)
    resultado = q.mod("Update material set tipo_unidad_id = %s, nombre = %s, precio = %s, updated_at = %s where id = %s",(valores[0],valores[1],valores[2],valores[3],valores[4]))
    return resultado
def eliminar_material(id):
    resultado = q.mod("Update material set estatus = %s where id = %s",(2,id))
    return resultado