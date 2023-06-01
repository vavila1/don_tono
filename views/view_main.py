import tkinter as tk
import tkinter.messagebox as messagebox
import sys
import os

directorio_actual = os.getcwd()
directorio_models = os.path.dirname(directorio_actual)
directorio_models+= "/models"
sys.path.append(directorio_models)

import model_sesion as sesion
import model_almacen as almacen
import model_tienda as tienda

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        
        self.label_email = tk.Label(self, text="Email")
        self.label_email.pack()
        
        self.entry_email = tk.Entry(self)
        self.entry_email.pack()
        
        self.label_password = tk.Label(self, text="Password")
        self.label_password.pack()
        
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack()
        
        self.btn_login = tk.Button(self, text="Login", command=self.login)
        self.btn_login.pack()
    
    def login(self):
        email = self.entry_email.get()
        password = self.entry_password.get()
        
        if sesion.verificar_contrasena([email, password]):
            self.destroy()
            MainWindow(email)
        else:
            messagebox.showerror("Error", "Credenciales inválidas")

class MainWindow(tk.Tk):
    def __init__(self, email):
        super().__init__()
        self.title("Menú Principal")
        
        self.label_welcome = tk.Label(self, text="Bienvenido, " + email)
        self.label_welcome.pack()
        
        self.btn_entrada_almacen = tk.Button(self, text="Entrada Almacén", command=self.entrada_almacen)
        self.btn_entrada_almacen.pack()
        
        self.btn_salida_almacen = tk.Button(self, text="Salida Almacén", command=self.salida_almacen)
        self.btn_salida_almacen.pack()
        
        self.btn_entrada_tiendas = tk.Button(self, text="Entrada Tiendas", command=self.entrada_tiendas)
        self.btn_entrada_tiendas.pack()
        
        self.btn_ventas = tk.Button(self, text="Ventas", command=self.ventas)
        self.btn_ventas.pack()
        
        self.btn_reportes = tk.Button(self, text="Reportes", command=self.reportes)
        self.btn_reportes.pack()
        
        self.btn_logout = tk.Button(self, text="Logout", command=self.logout)
        self.btn_logout.pack()
    
    def entrada_almacen(self):
        # Aquí puedes implementar la lógica para la acción de Entrada Almacén
        pass
    
    def salida_almacen(self):
        # Aquí puedes implementar la lógica para la acción de Salida Almacén
        pass
    
    def entrada_tiendas(self):
        # Aquí puedes implementar la lógica para la acción de Entrada Tiendas
        pass
    
    def ventas(self):
        # Aquí puedes implementar la lógica para la acción de Ventas
        pass
    
    def reportes(self):
        # Aquí puedes implementar la lógica para la acción de Reportes
        pass
    
    def logout(self):
        self.destroy()
        LoginWindow()

if __name__ == "__main__":
    login_window = LoginWindow()
    login_window.mainloop()
