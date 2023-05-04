from tkinter import *
from tkinter import ttk

def ingresar(*args):
    try:
        print("El usuario:" +user.get() +" intento ingresar con la contraseña: "+ pwdr.get())
    except ValueError:
        pass

raiz = Tk()

user = StringVar();
pwdr = StringVar();

raiz.title("Inicio de Sesion")

#Definiendo el marco principal y estableciendo el grid
marcoPrincipal = ttk.Frame(raiz, padding="20 20 20 20")
marcoPrincipal.grid(column = 0,row = 0)

ttk.Label(marcoPrincipal, text = "Usuario:", width=18, anchor=E).grid(column=0, row=0)
ttk.Label(marcoPrincipal, text = "Contraseña:", width=18, anchor=E).grid(column=0, row=1)

txtUsr = ttk.Entry(marcoPrincipal, textvariable = user)
txtUsr.grid(column = 1, row = 0)

txtPwdr = ttk.Entry(marcoPrincipal, textvariable=pwdr, show="*")
txtPwdr.grid(column=1, row=1)

ttk.Button(marcoPrincipal,text = "Ingresar", command = ingresar).grid(column=1, row=2, sticky=E)

txtUsr.focus()

for hijo in marcoPrincipal.winfo_children():
    hijo.grid_configure(padx=5, pady=5)

raiz.mainloop()