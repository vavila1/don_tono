#Aqui se encuentra el modelo del inicio de sesion
import funciones_model as q

def verificar_contrasena(valores):
    resultado = q.select("Select cuenta.contra from cuenta where cuenta.correo ='"+str(valores[0]+"' AND cuenta.estatus = 1"))
    resultado = q.consulta_lista(resultado)
    if(resultado == []):
        return False
    resultado = resultado[0][0]
    return resultado == valores[1]

def info_cuenta(valores):
    resultado = q.select("SELECT  rol.id as rol_id , cuenta.id as cuenta_id, empleado.id as empleado_id from cuenta, rol, empleado where cuenta.rol_id = rol.id AND empleado.cuenta_id = cuenta.id AND cuenta.correo = '"+str(valores[0])+"'")
    resultado = q.consulta_lista(resultado)
    resultado = resultado[0]
    return resultado