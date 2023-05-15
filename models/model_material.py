import funciones_model as q
def crear_almacen(valores):
    valores.append(q.timestamp())
    resultado = q.mod("INSERT INTO almacen (nombre, direccion, created_at) VALUES (%s, %s, %s)",
                  (valores[0], valores[1], valores[2]))

    if(resultado == True):
        print("Éxito")
        consulta = q.select("Select * from almacen where almacen.nombre='"+str(valores[0])+"'")
        print(consulta)
    else:
        print("Fracaso")

valores = []
preguntas = ["Escribe el nombre del almacen","Escribe la direccion del almacen"]
for i in range(2):
    valor = input(preguntas[i]+"\n")
    valores.append(valor)
crear_almacen(valores)