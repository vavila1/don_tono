import tkinter as tk

def prueba2(ventana,frame_externo,funcion_externa):
    frame_externo.pack_forget()
    frame2 = tk.Frame(ventana, name="ejemplo2")
    btn2 = tk.Button(frame2,text="Boton2",command=lambda: funcion_externa(frame2,frame_externo))
    btn2.pack()
    frame2.pack()