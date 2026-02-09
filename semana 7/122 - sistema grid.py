from tkinter import *
ventana = Tk()
ventana.title("sistema grid")

label1 = Label(ventana, text="fila 0, columna 0")
label2 = Label(ventana, text="fila 0, columna 1")
label3 = Label(ventana, text="fila 1, columna 0")
label4 = Label(ventana, text="fila 1, columna 1")

label1.grid(row=0, column=0 padx=5, pady=5)
label2.grid(row=0, column=1 padx=5, pady=5)
label3.grid(row=0, column=0 padx=5, pady=5)
label4.grid(row=0, column=0 padx=5, pady=5)

entrada = Entry(ventana, front=("Arial",20))
entrada.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

ventana.mainloop()
