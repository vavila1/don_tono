import mysql.connector

# Establecer la conexión a la base de datos
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="gastos"
)

# Crear un objeto cursor para ejecutar consultas
cursor = conn.cursor()

# Ejecutar una consulta SQL
cursor.execute("SELECT * FROM cuenta")

# Obtener los resultados de la consulta
for row in cursor:
  print(row)

# Cerrar la conexión
conn.close()
