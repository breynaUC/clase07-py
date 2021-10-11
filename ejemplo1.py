'''
Ejercicio1: Construir un programa que calcule el factorial de un valor 
numérico introducido como parámetro.
'''
from tkinter import *
win = Tk()
'''El siguiente codigo permite centrar el formulario en la pantalla de 
la computadora.'''
x = (win.winfo_screenwidth() - win.winfo_reqwidth()) / 2
y = (win.winfo_screenheight() - win.winfo_reqheight()) / 2
win.geometry("+%d+%d" % (x, y))
'''El siguiente código es para el tamaño de la pantalla.'''
win.geometry('300x200')
'''Funcion que calcula el factorial de un numero'''
num = IntVar()
def factorial(numero):
    if numero <= 0:
        return 1
    fact = 1
    while numero > 0:
        fact = fact * numero
        numero -= 1
    return fact
def calcular():
    text.insert('1.0',factorial(num.get()))

def limpiar():
    text.delete("1.0","end")
    entry_numero.delete(0, END)
    entry_numero.focus()

label_numero = Label(win, text="Número: ")
label_numero.grid(column=1, row=1, sticky=E)
entry_numero = Entry(win, textvariable=num, width=30)
entry_numero.grid(row=1, column=2, sticky=E+W)
boton_calcular = Button(win, text="Calcular", command=calcular, background="green", fg='white', 
relief="groove", borderwidth=5)
boton_calcular.grid(row=3,column=2, sticky=N+W, pady=10)
boton_limpiar = Button(win, text="Limpiar", command=limpiar, background="red", fg='white', 
relief="groove", borderwidth=5)
boton_limpiar.grid(row=3,column=2, sticky=NE, pady=10)
text = Text(win, width=30, height=5, font=('Time', 12), wrap='word', fg='#4A7A8C')
text.grid(columnspan=6, pady=11, padx=13)
win.mainloop()