from tkinter import *
from tkinter import ttk

def calcular(*args):
    try:
        resultado = float(pies.get()) * 0.3048
        metros.set(resultado)
    except ValueError:
        pass

raiz = Tk()
#Actualizando el titulo de la ventana
raiz.title("Pies a metros")

#Definiendo el marco principal y estableciendo el grid
marcoPrincipal = ttk.Frame(raiz, padding="20 20 20 20")
marcoPrincipal.grid(column = 0,row = 0)

#inputs/ouputs
pies = StringVar()
metros = StringVar()

#Linea de texto
txtPies = ttk.Entry(marcoPrincipal, textvariable = pies)
txtPies.grid(column = 1, row = 0)

#label no necesita una variable para el objeto, objeto anonimo
ttk.Label(marcoPrincipal, text = "Pies").grid(column=2, row=0, pady=10)
ttk.Label(marcoPrincipal, text = "Equivalente a").grid(column=0, row=1)
ttk.Label(marcoPrincipal, textvariable=metros).grid(column=1, row=1)
ttk.Label(marcoPrincipal, text = "Metros").grid(column=2, row=1, sticky=(N, W))

#el Boton ejecuta la funcion que se le pasa en el parametro command
ttk.Button(marcoPrincipal,text = "Calcular", command = calcular).grid(column=2, row=2, pady=10)


#agregando padding  a todos los hijos

for hijo in marcoPrincipal.winfo_children():
    hijo.grid_configure(padx=5, pady=5)

#Estableciendo el cursor en el textfield
txtPies.focus()
#Detectando el enter
raiz.bind("<Return>",calcular)

#Mostrando la ventana en un ciclo infinito que permite escuchar eventos
raiz.mainloop()


