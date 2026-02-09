from tkinter import Tk, Entry, Button, END


class Calculadora:

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")

        self.e_texto = Entry(self.ventana, font=("calibri", 20), justify="right")
        self.e_texto.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.i = 0
        self.crear_botones()

    def click_boton(self, valor):
        self.e_texto.insert(self.i, valor)
        self.i += 1

    def borrar(self):
        self.e_texto.delete(0, END)
        self.i = 0

    def hacer_operacion(self):
        try:
            ecuacion = self.e_texto.get()
            resultado = eval(ecuacion)
            self.e_texto.delete(0, END)
            self.e_texto.insert(0, resultado)
            self.i = len(str(resultado))
        except:
            self.e_texto.delete(0, END)
            self.e_texto.insert(0, "Error")
            self.i = 0

    def crear_botones(self):
        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('AC', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('/', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for texto, fila, columna in botones:
            if texto == 'AC':
                boton = Button(self.ventana, text=texto, width=5, height=2,
                               command=self.borrar)
            elif texto == '=':
                boton = Button(self.ventana, text=texto, width=5, height=2,
                               command=self.hacer_operacion)
            else:
                boton = Button(
                    self.ventana,
                    text=texto,
                    width=5,
                    height=2,
                    command=lambda t=texto: self.click_boton(t)
                )

            boton.grid(row=fila, column=columna, padx=3, pady=3)


root = Tk()
app = Calculadora(root)
root.mainloop()
