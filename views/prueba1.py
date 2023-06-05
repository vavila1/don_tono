import tkinter as tk
import view_tipo_operacion
def salir(ventana_menu_principal):
    ventana_menu_principal.quit()
def regresar_de_menu_tipos_de_operacion(frame_menu_tipos_de_operacion,frame_menu_principal):
    frame_menu_tipos_de_operacion.pack_forget()
    frame_menu_principal.pack()
def crear_frame_menu_principal(ventana_menu_principal):
    frame_menu_principal = tk.Frame(ventana_menu_principal)
    btn_menu_tipos_de_operacion = tk.Button(frame_menu_principal,text="Tipos de Operacion",command=lambda: view_tipo_operacion.crear_frame_menu_tipos_de_operacion(ventana_menu_principal,frame_menu_principal,regresar_de_menu_tipos_de_operacion))
    btn_menu_tipos_de_operacion.pack()
    btn_salir = tk.Button(frame_menu_principal,text="Salir",command=lambda: salir(ventana_menu_principal))
    btn_salir.pack(side="top",padx=200,pady=10)
    frame_menu_principal.pack()
ventana_menu_principal = tk.Tk()
ventana_menu_principal.geometry("600x600")
crear_frame_menu_principal(ventana_menu_principal)
ventana_menu_principal.mainloop()
