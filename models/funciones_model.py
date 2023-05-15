import mysql.connector
import datetime
def conexion():
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="don_tono"
    )
    return conn
def select(sql):
    resultados = []
    conn = conexion()
    # Crear un objeto cursor para ejecutar consultas
    cursor = conn.cursor()

    # Ejecutar una consulta SQL
    cursor.execute(sql)

    # Obtener los resultados de la consulta
    for row in cursor:
        resultados.append(row)

    # Cerrar la conexión
    conn.close()
    return resultados

#Funcion que obtiene el timestamp
def timestamp():
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime
#Funcion para convertir  el resultado de la consulta en lista
def consulta_lista(resultado):
    lista = []
    for row in resultado:
        lista.append(list(row))
    return lista

def mod(sql,valores):
    conn = conexion()
    cursor = conn.cursor()
    try:
        cursor.execute(sql,valores)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(e)
        conn.rollback()  # Revertir los cambios en caso de error
        return False


