from tkinter import *
from tkinter import ttk

raiz = Tk()

raiz.title("Muestra de Widgets")

marcoPrincipal = ttk.Frame(raiz, padding="10 10 10 10")
marcoPrincipal.grid(column = 0,row = 0)

marcoNombre = ttk.Frame(marcoPrincipal,width=340,height=180,relief=RAISED, border=10)
marcoAficiones = ttk.Frame(marcoPrincipal, width=340,height=60,relief=RAISED, border=10, padding="28 0 0 0")
marcoOcupacion = ttk.Frame(marcoPrincipal)
marcoEstado = ttk.Frame(marcoPrincipal)
marcoBotones = ttk.Frame(marcoPrincipal, width=340,height=30)

marcoNombre.grid(column=0, row=0)
marcoAficiones.grid(column=0, row=1)
marcoBotones.grid(column=0, row=2)
marcoOcupacion.grid(column=1, row=0)
marcoEstado.grid(column=1, row=1)

marcoNombre.grid_propagate(0)
marcoAficiones.grid_propagate(0)
marcoBotones.grid_propagate(0)

ttk.Label(marcoNombre, text = "Nombre:", width=15, anchor=W).grid(column=0, row=0)
ttk.Label(marcoNombre, text = "A. Paterno:", width=15, anchor=W).grid(column=0, row=1)
ttk.Label(marcoNombre, text = "A. Materno:", width=15, anchor=W).grid(column=0, row=2)
ttk.Label(marcoNombre, text = "Correo:", width=15, anchor=W).grid(column=0, row=3)
ttk.Label(marcoNombre, text = "Móvil:", width=15, anchor=W).grid(column=0, row=4)

txtNombre = ttk.Entry(marcoNombre, width=30)
txtAPat = ttk.Entry(marcoNombre, width=30)
txtAMat = ttk.Entry(marcoNombre, width=30)
txtCorreo = ttk.Entry(marcoNombre,width=30)
txtMovil = ttk.Entry(marcoNombre, width=30)

txtNombre.grid(column = 1, row = 0)
txtAPat.grid(column = 1, row = 1)
txtAMat.grid(column = 1, row = 2)
txtCorreo.grid(column = 1, row = 3)
txtMovil.grid(column = 1, row = 4)

ttk.Label(marcoAficiones, text = "Aficiones:", width=12).grid(column=0, row=0, sticky=W)

checkvar1=IntVar()
checkvar2=IntVar()
checkvar3=IntVar()

cbLeer= ttk.Checkbutton(marcoAficiones, text="Leer",variable=checkvar1, width=12)
cbMusica = ttk.Checkbutton(marcoAficiones, text="Música", variable=checkvar2, width=12)
cbVideo = ttk.Checkbutton(marcoAficiones, text="Videojuegos", variable=checkvar3, width=12)



cbLeer.grid(column=0, row=1, sticky=W)
cbMusica.grid(column=1, row=1, sticky=W)
cbVideo.grid(column=2, row=1, sticky=W)



ttk.Button(marcoBotones,text = "Guardar").grid(column=0, row=0, sticky=W)
ttk.Button(marcoBotones,text = "Cancelar").grid(column=1, row=0, sticky=W, padx=60)

rbEstudiante = ttk.Radiobutton(marcoOcupacion, text="Estudiante")
rbEmpleado = ttk.Radiobutton(marcoOcupacion, text="Empleado")
rbDesempleado = ttk.Radiobutton(marcoOcupacion, text="Desempleado")

rbEstudiante.grid(column=0, row=0, sticky=W)
rbEmpleado.grid(column=0, row=1, sticky=W)
rbDesempleado.grid(column=0, row=2 , sticky=W)


cbEstados = ttk.Combobox(marcoEstado)
cbEstados.grid(column=0, row=0)
cbEstados['values']=("Aguascalientes","Baja California","Baja California Sur","Campeche","Chiapas","Chihuahua","Coahuila","Colima",
"Distrito Federal","Durango","Guanajuato","Guerrero","Hidalgo","Jalisco","México","Michoacán","Morelos","Nayarit","Nuevo León",
"Oaxaca","Puebla","Querétaro","Quintana Roo","San Luis Potosí","Sinaloa","Sonora","Tabasco","Tamaulipas","Tlaxcala","Veracruz",
"Yucatán","Zacatecas")

cbEstados.set("Estados (32)")

for hijo in marcoPrincipal.winfo_children():
    hijo.grid_configure(padx=10, pady=10)

for hijo in marcoNombre.winfo_children():
    hijo.grid_configure(padx=5, pady=5)

raiz.mainloop()