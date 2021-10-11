"""
Registrar el nombre y edad de los estudiantes de un colegio.
Luego calcular la suma de las edades. 
Imprimir los estudiantes con su edad
y la suma de las edades.
"""
from tkinter import *
win = Tk()
'''El siguiente codigo permite centrar el formulario en la pantalla de 
la computadora.'''
x = (win.winfo_screenwidth() - win.winfo_reqwidth()) / 2
y = (win.winfo_screenheight() - win.winfo_reqheight()) / 2
win.geometry("+%d+%d" % (x, y))
'''El siguiente código es para el tamaño de la pantalla.'''
win.geometry('300x250')
'''Funcion que calcula el factorial de un numero'''
nombre = StringVar()
edad = IntVar()
datos={}
def agregar():
    datos[nombre.get()]=edad.get()
    entry_nombre.delete(0, END)
    entry_edad.delete(0, END)
    entry_nombre.focus() 
    
def imprimir():
    text.insert("insert", "Datos= ")
    text.insert("insert", datos)
    total = 0
    for i in datos.values():
        total += i
    text.insert("end", "\nSuma de edades: "+str(total))


def limpiar():
    text.delete("1.0","end")
    entry_nombre.focus()

label_nombre = Label(win, text="Nombre: ")
label_nombre.grid(column=1, row=1, sticky=E)
entry_nombre = Entry(win, textvariable=nombre, width=30)
entry_nombre.grid(row=1, column=2, sticky=E+W)
label_edad = Label(win, text="Edad: ")
label_edad.grid(column=1, row=2, sticky=E)
entry_edad = Entry(win, textvariable=edad, width=30)
entry_edad.grid(row=2, column=2, sticky=E+W)

boton_calcular = Button(win, text="Agregar", command=agregar, background="green", fg='white', 
relief="groove", borderwidth=5)
boton_calcular.grid(row=3,column=2, sticky=NW, pady=10)
boton_limpiar = Button(win, text="Imprimir", command=imprimir, background="yellow", fg='black', 
relief="groove", borderwidth=5)
boton_limpiar.grid(row=3,column=2, sticky=N, pady=10)
boton_imprimir = Button(win, text="Limpiar", command=limpiar, background="red", fg='white', 
relief="groove", borderwidth=5, padx=2)
boton_imprimir.grid(row=3,column=2, sticky=NE, pady=10)
text = Text(win, width=38, height=7, font=('Time', 10), wrap='word', fg='#4A7A8C')
text.grid(columnspan=6, pady=11, padx=13)

win.mainloop()