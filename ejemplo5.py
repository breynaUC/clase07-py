
from tkinter import *
import math
win = Tk()
x = (win.winfo_screenwidth() - win.winfo_reqwidth()) / 2
y = (win.winfo_screenheight() - win.winfo_reqheight()) / 2
win.geometry("+%d+%d" % (x, y))
win.geometry('300x300')
num = IntVar()
res = IntVar()
def calcular():    
    res.set(math.sqrt(num.get()))

label_numero = Label(win, text="Número: ")
label_numero.grid(row=0, column=0)
entry_numero = Entry(win, textvariable=num, width=30)
entry_numero.grid(row=0, column=1)
boton_calcular = Button(win, text="Calcular", command=calcular, background="green", fg='white', 
relief="groove", borderwidth=5)
label_numero = Label(win, text="Resultado: ")
label_numero.grid(row=2, column=0)
boton_calcular.grid(row=1,column=1, sticky=NE, pady=5)
entry_res = Entry(win, textvariable=res, width=30)
entry_res.grid(row=2, column=1)
win.mainloop()