import tkinter as tk

# Crear una instancia de la ventana principal
ventana = tk.Tk()

# Configurar propiedades de la ventana
ventana.title("Mi Ventana")
ventana.geometry("400x300")

# Agregar elementos a la ventana
etiqueta = tk.Label(ventana, text="¡Hola, mundo!")
etiqueta.pack()

boton = tk.Button(ventana, text="Haz clic")
boton.pack()

# Iniciar el bucle de eventos de la ventana
ventana.mainloop()
