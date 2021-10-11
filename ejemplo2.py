"""
Leer un número entero positivo desde teclado e 
imprimir la suma de los dígitos que lo componen.
"""
from tkinter import *
win = Tk()
'''El siguiente codigo permite centrar el formulario en la pantalla de 
la computadora.'''
x = (win.winfo_screenwidth() - win.winfo_reqwidth()) / 2
y = (win.winfo_screenheight() - win.winfo_reqheight()) / 2
win.geometry("+%d+%d" % (x, y))
'''El siguiente código es para el tamaño de la pantalla.'''
win.geometry('300x200')
#============
#variables
num = IntVar()
res = IntVar()
#============
def calcular():
    n = num.get() 
    suma=0
    while n!=0:
        digito=n%10
        suma+=digito
        n=n//10
    res.set(suma)

#============
label_numero = Label(win, text="Número: ")
label_numero.grid(column=1, row=1, sticky=E)
entry_numero = Entry(win, textvariable=num, width=30)
entry_numero.grid(row=1, column=2, sticky=E+W)
boton_calcular = Button(win, text="Calcular", command=calcular, background="green", fg='white', 
relief="groove", borderwidth=5)
boton_calcular.grid(row=3,column=2, sticky=N+W, pady=10)
label_numero = Label(win, text="Resultado: ")
label_numero.grid(column=1, row=4, sticky=E)
entry_resultado = Entry(win, textvariable=res, width=30)
entry_resultado.grid(row=4, column=2, sticky=E+W)
win.mainloop()