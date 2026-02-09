from tkinter import *

ventana = Tk()
ventana.title("Calculadora")

e_texto = Entry(ventana, front=('Calibri 20'))
e_texto.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

button1 = Button(ventana, text="1", width=5, height=2)
button2 = Button(ventana, text="2", width=5, height=2)
button3 = Button(ventana, text="3", width=5, height=2)
button4 = Button(ventana, text="4", width=5, height=2)
button5 = Button(ventana, text="5", width=5, height=2)
button6 = Button(ventana, text="6", width=5, height=2)
button7 = Button(ventana, text="7", width=5, height=2)
button8 = Button(ventana, text="8", width=5, height=2)
button9 = Button(ventana, text="9", width=5, height=2)
button0 = Button(ventana, text="*", width=5, height=2)

boton_borrar = Button(ventana, text="-", width=5, height=2)
boton_parentesis1 = Button(ventana, text="(", width=5, height=2)
boton_parentesis2 = Button(ventana, text=")", width=5, height=2)
boton_parentesis3 = Button(ventana, text=")", width=5, height=2)
boton_punto = Button(ventana, text=".", width=5, height=2)

boton_div = Button(ventana, text="/", width=5, height=2)
boton_mult = Button(ventana, text="*", width=5, height=2)
boton_sum = Button(ventana, text="+", width=5, height=2)
boton_rest = Button(ventana, text="-", width=5, height=2)
boton_igual = Button(ventana, text="=", width=5, height=2)

boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_parentesis1.grid(row=1, column=1, padx=5, pady=5)
boton_parentesis2.grid(row=1, column=2, padx=5, pady=5)
boton_div.grid(row=1, column=3, padx=5, pady=5)

button7.grid(row=2, column=0, padx=5, pady=5)
button8.grid(row=2, column=1, padx=5, pady=5)
button9.grid(row=2, column=2, padx=5, pady=5)
boton_mult.grid(row=2, column=3, padx=5, pady=5)

ventana.mainloop()