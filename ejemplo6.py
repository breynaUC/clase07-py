from tkinter import *
win = Tk()
'''El siguiente codigo permite centrar el formulario en la pantalla de 
la computadora.'''
x = (win.winfo_screenwidth() - win.winfo_reqwidth()) / 2
y = (win.winfo_screenheight() - win.winfo_reqheight()) / 2
win.geometry("+%d+%d" % (x, y))
'''El siguiente código es para el tamaño de la pantalla.'''
win.geometry('300x250')
lista=[]
numero = IntVar()
def agregar():
    lista.append(numero.get())
    entry_numero.delete(0, END)
    entry_numero.focus() 
def limpiar():
    text.delete("1.0","end")
    entry_numero.focus()
def imprimir():
    text.insert("insert", "lista= ")
    text.insert("insert", lista)
    total = 0
    for i in lista:
        total += i
    text.insert("end", "\nSuma de números: "+str(total))
    text.insert("end", "\nPromedio: "+str(total/len(lista)))

label_numero = Label(win, text="Número: ")
label_numero.grid(column=1, row=1, sticky=E)
entry_numero = Entry(win, textvariable=numero, width=30)
entry_numero.grid(row=1, column=2, sticky=E+W)


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