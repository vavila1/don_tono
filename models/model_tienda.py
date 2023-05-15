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
    resultado = q.select("Select * from almacen where id ="+str(id)+"AND status=1")
    resultado = q.consulta_lista(resultado)
    return resultado[0]
def editar_tienda(id,valores):
    #esto sirve para agregar el id al final de la lista ya que asi es la sintaxis para agregar valores a la consulta
    valores.append(id)
    resultado = q.mod("Update tienda set nombre = %s, direccion = %s, updated_at = %s where id = %s",(valores[0],valores[1],valores[2],valores[3]))
    return resultado
def eliminar_tienda(id):
    resultado = q.mod("Update tienda set estatus = %s where id = %s",(2,id))
    return resultado

resultado = eliminar_tienda(1)
if(resultado == True):
    print("Se ha eliminado con exito la tienda")
else:
    print("Ha ocurrido un error al eliminar la tienda")