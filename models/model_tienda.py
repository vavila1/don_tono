#Aqui se encuentra CRUD tienda
import funciones_model as q

def crear_tienda(valores):
    valores.append(q.timestamp())
    resultado = q.mod("INSERT INTO tienda (nombre, direccion, estatus, created_at) VALUES (%s, %s, %s,%s)",
                  (valores[0], valores[1], valores[2],valores[3]))
    return resultado
def leer_tiendas():
    resultado = q.select('Select * from tienda where estatus = 1')
    resultado = q.consulta_lista(resultado)
    return resultado
def leer_tienda(id):
    consulta = "Select * from tienda where id = "+str(id)+" AND estatus = 1"
    resultado = q.select(consulta)
    resultado = q.consulta_lista(resultado)
    if(resultado != []):
        return resultado[0]
    return resultado
def editar_tienda(id,valores):
    #esto sirve para agregar el id al final de la lista ya que asi es la sintaxis para agregar valores a la consulta
    valores.append(q.timestamp())
    valores.append(id)
    resultado = q.mod("Update tienda set nombre = %s, direccion = %s, updated_at = %s where id = %s",(valores[0],valores[1],valores[2],valores[3]))
    return resultado
def eliminar_tienda(id):
    resultado = q.mod("Update tienda set estatus = %s where id = %s",(2,id))
    return resultado