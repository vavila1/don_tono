#Aqui se encuentra CRUD cuenta
import funciones_model as q

def crear_cuentas(valores):
    valores.append(q.timestamp())
    resultado = q.mod("INSERT INTO cuenta (rol_id, correo, contra, estatus, created_at) VALUES (%s, %s, %s, %s, %s)",
                  (valores[0], valores[1],valores[2],valores[3],valores[4]))
    return resultado
    
def leer_cuentas():
    resultado = q.select('Select cuenta.id as id, rol.nombre as rol, cuenta.correo, cuenta.contra, cuenta.created_at from cuenta,rol where cuenta.estatus = 1 AND cuenta.rol_id = rol.id')
    resultado = q.consulta_lista(resultado)
    return resultado
def leer_cuenta(id):
    consulta = "Select cuenta.id as id, rol.nombre as rol, rol.id as id_rol, cuenta.correo, cuenta.contra, cuenta.created_at from rol,cuenta where cuenta.id = "+str(id)+" AND cuenta.estatus = 1 AND cuenta.rol_id = rol.id"
    resultado = q.select(consulta)
    resultado = q.consulta_lista(resultado)
    if(resultado != []):
        return resultado[0]
    return resultado

def leer_cuenta_correo(correo):
    consulta = "Select cuenta.id as id, rol.nombre as rol, rol.id as id_rol, cuenta.correo, cuenta.contra, cuenta.created_at from rol,cuenta where cuenta.correo = '"+correo+"' AND cuenta.estatus = 1 AND cuenta.rol_id = rol.id"
    print(consulta)
    resultado = q.select(consulta)
    resultado = q.consulta_lista(resultado)
    if(resultado != []):
        return resultado[0]
    return resultado

def leer_ultimo_id(correo):
    consulta = "Select cuenta.id as id, rol.nombre as rol, rol.id as id_rol, cuenta.correo, cuenta.contra, cuenta.created_at from rol,cuenta where cuenta.correo = '"+correo+"' AND cuenta.estatus = 1 AND cuenta.rol_id = rol.id"
    resultado = q.select(consulta)
    print(resultado)
    id_cuenta = resultado[0][0]
    print(id_cuenta)
    return id_cuenta
    
def editar_cuenta(id,valores):
    #esto sirve para agregar el id al final de la lista ya que asi es la sintaxis para agregar valores a la consulta
    valores.append(q.timestamp())
    valores.append(id)
    resultado = q.mod("Update cuenta set rol_id = %s, correo = %s, contra = %s, updated_at = %s where id = %s",(valores[0],valores[1],valores[2],valores[3],valores[4]))
    return resultado
def eliminar_cuenta(id):
    resultado = q.mod("Update cuenta set estatus = %s where id = %s",(2,id))
    return resultado