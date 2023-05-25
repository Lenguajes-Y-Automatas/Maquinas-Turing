from tkinter import *
from tkinter import messagebox
import re
import time

from maquina_de_turing import maquina
from TuringMachine import TuringMachine

class Interfaz:
    def __init__(self) -> None:
        pass

    def ventana(self):
        self.mainwindow = Tk()

        ancho_ventana = 420
        alto_ventana = 550
        x_ventana = self.mainwindow.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.mainwindow.winfo_screenheight()// 2 - alto_ventana // 2 - 42
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.mainwindow.geometry(posicion)

        self.mainwindow.title('Máquina de Turing')
        #self.mainwindow.resizable(0, 0)
        self.mainwindow.config(bg='#7FADA9')

        # Título
        titulo = Label(self.mainwindow, text='Máquina de Turing', font=('JetBrains Mono', 20), bg='#7FADA9').grid(row=0, column=0, columnspan=11, pady=10)

        # Entradas
        cinta1 = Label(self.mainwindow, text='Cinta 1:', font=('JetBrains Mono', 15), bg='#7FADA9').grid(row=1, column=0, columnspan=11, padx=10)

        self.cinta1 = StringVar()
        entrada_texto = Entry(self.mainwindow, font=('JetBrains Mono', 15), width=30, textvariable=self.cinta1).grid(row=2, column=0, padx=10, columnspan=11)

        cinta2 = Label(self.mainwindow, text='Cinta 2:', font=('JetBrains Mono', 15), bg='#7FADA9').grid(row=3, column=0, pady=10, padx=10, columnspan=11)

        self.cinta2 = StringVar()
        entrada_texto2 = Entry(self.mainwindow, font=('JetBrains Mono', 15), width=30, textvariable=self.cinta2).grid(row=4, column=0, pady=10, padx=10, columnspan=11)

        # Botones
        boton = Button(self.mainwindow, width=15, text='Evualuar', font=('JetBrains Mono', 15), bg='#22b814', fg='#ffffff',activebackground='#1a8a0f', activeforeground='#fff', relief='flat', borderwidth=0, command=self.envio).grid(row=5, column=0, pady=10, padx=10, columnspan=11)

        boton2 = Button(self.mainwindow, width=15, text='Limpiar', font=('JetBrains Mono', 15), bg='#ff0000', fg='#ffffff',activebackground='#990000', activeforeground='#fff', relief='flat', borderwidth=0, command=self.limpiar).grid(row=6, column=0, pady=10, padx=10, columnspan=11)

        #* Etiquetas de salida: Primera fila
        self.c1f1 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c1f1.grid(row=10, column=10, padx=10)

        self.c1f2 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c1f2.grid(row=11, column=10, padx=10)

        self.c1f3 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c1f3.grid(row=12, column=10, padx=10)

        self.c1f4 = Label(self.mainwindow, text='-', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c1f4.grid(row=13, column=10, padx=10)

        #* Segunda fila
        self.c2f1 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c2f1.grid(row=10, column=9, padx=10)

        self.c2f2 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c2f2.grid(row=11, column=9, padx=10)

        self.c2f3 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c2f3.grid(row=12, column=9, padx=10)

        self.c2f4 = Label(self.mainwindow, text='-', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c2f4.grid(row=13, column=9, padx=10)

        #* Tercera fila
        self.c3f1 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c3f1.grid(row=10, column=8, padx=10)

        self.c3f2 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c3f2.grid(row=11, column=8, padx=10)

        self.c3f3 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c3f3.grid(row=12, column=8, padx=10)

        self.c3f4 = Label(self.mainwindow, text='-', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c3f4.grid(row=13, column=8, padx=10)

        #* Cuarta fila
        self.c4f1 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c4f1.grid(row=10, column=7, padx=10)

        self.c4f2 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c4f2.grid(row=11, column=7, padx=10)

        self.c4f3 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c4f3.grid(row=12, column=7, padx=10)

        self.c4f4 = Label(self.mainwindow, text='-', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c4f4.grid(row=13, column=7, padx=10)

        #* Quinta fila
        self.c5f1 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c5f1.grid(row=10, column=6, padx=10)

        self.c5f2 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c5f2.grid(row=11, column=6, padx=10)

        self.c5f3 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c5f3.grid(row=12, column=6, padx=10)

        self.c5f4 = Label(self.mainwindow, text='-', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c5f4.grid(row=13, column=6, padx=10)

        #* Sexta fila
        self.c6f1 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c6f1.grid(row=10, column=5, padx=10)

        self.c6f2 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c6f2.grid(row=11, column=5, padx=10)

        self.c6f3 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c6f3.grid(row=12, column=5, padx=10)

        self.c6f4 = Label(self.mainwindow, text='-', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c6f4.grid(row=13, column=5, padx=10)

        #* Séptima fila
        self.c7f1 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c7f1.grid(row=10, column=4, padx=10)

        self.c7f2 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c7f2.grid(row=11, column=4, padx=10)

        self.c7f3 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c7f3.grid(row=12, column=4, padx=10)

        self.c7f4 = Label(self.mainwindow, text='-', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c7f4.grid(row=13, column=4, padx=10)

        #* Octava fila

        self.c8f1 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c8f1.grid(row=10, column=3, padx=10)

        self.c8f2 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c8f2.grid(row=11, column=3, padx=10)

        self.c8f3 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c8f3.grid(row=12, column=3, padx=10)

        self.c8f4 = Label(self.mainwindow, text='-', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c8f4.grid(row=13, column=3, padx=10)

        #* Novena fila
        self.c9f1 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c9f1.grid(row=10, column=2, padx=10)

        self.c9f2 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c9f2.grid(row=11, column=2, padx=10)

        self.c9f3 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c9f3.grid(row=12, column=2, padx=10)

        self.c9f4 = Label(self.mainwindow, text='-', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c9f4.grid(row=13, column=2, padx=10)

        #* Décima fila
        self.c10f1 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c10f1.grid(row=10, column=1, padx=10)

        self.c10f2 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c10f2.grid(row=11, column=1, padx=10)

        self.c10f3 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c10f3.grid(row=12, column=1, padx=10)

        self.c10f4 = Label(self.mainwindow, text='-', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c10f4.grid(row=13, column=1, padx=10)

        #* Undécima fila
        self.c11f1 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c11f1.grid(row=10, column=0, padx=10)

        self.c11f2 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c11f2.grid(row=11, column=0, padx=10)

        self.c11f3 = Label(self.mainwindow, text='0', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c11f3.grid(row=12, column=0, padx=10)

        self.c11f4 = Label(self.mainwindow, text='-', font=('JetBrains Mono', 15), bg='#b6bfca')
        self.c11f4.grid(row=13, column=0, padx=10)
        self.mainwindow.mainloop()

    def envio(self):
        cinta1 = self.cinta1.get()
        cinta2 = self.cinta2.get()

        #* Valida que las cajas de texto no esten vacias
        if cinta1 != '' or cinta2 != '':
            #* valida que las cintas solo contengan un máximo de 10
            len_cinta1 = len(cinta1)
            len_cinta2 = len(cinta2)

            if len_cinta1 <= 10 and len_cinta2 <= 10:
                #* Verifica que la cinta solo contenga 0 y 1
                flag_cinta1 = False
                flag_cinta2 = False
                
                if re.sub("[^01]", "", cinta1) == cinta1:
                    flag_cinta1 = True

                if re.sub("[^01]", "", cinta2) == cinta2:
                    flag_cinta2 = True

                if flag_cinta1 and flag_cinta2:
                    maquina = TuringMachine()
                    listado = maquina.create_tapes(cinta1, cinta2)

                    #* Etiquetas de salida: Primera fila
                    self.c1f1.config(text=listado[10][0], bg='#b6bfca')
                    self.c1f2.config(text=listado[10][1], bg='#b6bfca')
                    self.c1f3.config(text=listado[10][2], bg='#b6bfca')
                    self.c1f4.config(text=listado[10][3], bg='#b6bfca')

                    #* Segunda fila
                    self.c2f1.config(text=listado[9][0], bg='#b6bfca')
                    self.c2f2.config(text=listado[9][1], bg='#b6bfca')
                    self.c2f3.config(text=listado[9][2], bg='#b6bfca')
                    self.c2f4.config(text=listado[9][3], bg='#b6bfca')

                    #* Tercera fila
                    self.c3f1.config(text=listado[8][0], bg='#b6bfca')
                    self.c3f2.config(text=listado[8][1], bg='#b6bfca')
                    self.c3f3.config(text=listado[8][2], bg='#b6bfca')
                    self.c3f4.config(text=listado[8][3], bg='#b6bfca')

                    #* Cuarta fila
                    self.c4f1.config(text=listado[7][0], bg='#b6bfca')
                    self.c4f2.config(text=listado[7][1], bg='#b6bfca')
                    self.c4f3.config(text=listado[7][2], bg='#b6bfca')
                    self.c4f4.config(text=listado[7][3], bg='#b6bfca')
                    #* Quinta fila
                    self.c5f1.config(text=listado[6][0], bg='#b6bfca')
                    self.c5f2.config(text=listado[6][1], bg='#b6bfca')
                    self.c5f3.config(text=listado[6][2], bg='#b6bfca')
                    self.c5f4.config(text=listado[6][3], bg='#b6bfca')

                    #* Sexta fila
                    self.c6f1.config(text=listado[5][0], bg='#b6bfca')
                    self.c6f2.config(text=listado[5][1], bg='#b6bfca')
                    self.c6f3.config(text=listado[5][2], bg='#b6bfca')
                    self.c6f4.config(text=listado[5][3], bg='#b6bfca')

                    #* Séptima fila
                    self.c7f1.config(text=listado[4][0], bg='#b6bfca')
                    self.c7f2.config(text=listado[4][1], bg='#b6bfca')
                    self.c7f3.config(text=listado[4][2], bg='#b6bfca')
                    self.c7f4.config(text=listado[4][3], bg='#b6bfca')

                    #* Octava fila
                    self.c8f1.config(text=listado[3][0], bg='#b6bfca')
                    self.c8f2.config(text=listado[3][1], bg='#b6bfca')
                    self.c8f3.config(text=listado[3][2], bg='#b6bfca')
                    self.c8f4.config(text=listado[3][3], bg='#b6bfca')

                    #* Novena fila
                    self.c9f1.config(text=listado[2][0], bg='#b6bfca')
                    self.c9f2.config(text=listado[2][1], bg='#b6bfca')
                    self.c9f3.config(text=listado[2][2], bg='#b6bfca')
                    self.c9f4.config(text=listado[2][3], bg='#b6bfca')

                    #* Décima fila
                    self.c10f1.config(text=listado[1][0], bg='#b6bfca')
                    self.c10f2.config(text=listado[1][1], bg='#b6bfca')
                    self.c10f3.config(text=listado[1][2], bg='#b6bfca')
                    self.c10f4.config(text=listado[1][3], bg='#b6bfca')

                    #* Undécima fila
                    self.c11f1.config(text=listado[0][0], bg='#b6bfca')
                    self.c11f2.config(text=listado[0][1], bg='#b6bfca')
                    self.c11f3.config(text=listado[0][2], bg='#b6bfca')
                    self.c11f4.config(text=listado[0][3], bg='#b6bfca')
                    
                    time.sleep(0.35)
                    pool = maquina.steps()
                    self.actualizar(pool)

                else:
                    messagebox.showerror('Error', 'Solo se permiten 0 y 1 en las cintas')
            else:
                messagebox.showerror('Error', 'Solo se permiten 10 caracteres por cinta')
        else:
            messagebox.showerror('Error', 'No puedes dejar las cintas vacías')

    def limpiar(self):
        #limpia las cajas de texto
        self.cinta1.set('')
        self.cinta2.set('')

        self.c1f1.config(text='0', bg='#b6bfca')
        self.c1f2.config(text='0', bg='#b6bfca')
        self.c1f3.config(text='0', bg='#b6bfca')
        self.c1f4.config(text='-', bg='#b6bfca')

        self.c2f1.config(text='0', bg='#b6bfca')
        self.c2f2.config(text='0', bg='#b6bfca')
        self.c2f3.config(text='0', bg='#b6bfca')
        self.c2f4.config(text='-', bg='#b6bfca')

        self.c3f1.config(text='0', bg='#b6bfca')
        self.c3f2.config(text='0', bg='#b6bfca')
        self.c3f3.config(text='0', bg='#b6bfca')
        self.c3f4.config(text='-', bg='#b6bfca')

        self.c4f1.config(text='0', bg='#b6bfca')
        self.c4f2.config(text='0', bg='#b6bfca')
        self.c4f3.config(text='0', bg='#b6bfca')
        self.c4f4.config(text='-', bg='#b6bfca')

        self.c5f1.config(text='0', bg='#b6bfca')
        self.c5f2.config(text='0', bg='#b6bfca')
        self.c5f3.config(text='0', bg='#b6bfca')
        self.c5f4.config(text='-', bg='#b6bfca')

        self.c6f1.config(text='0', bg='#b6bfca')
        self.c6f2.config(text='0', bg='#b6bfca')
        self.c6f3.config(text='0', bg='#b6bfca')
        self.c6f4.config(text='-', bg='#b6bfca')

        self.c7f1.config(text='0', bg='#b6bfca')
        self.c7f2.config(text='0', bg='#b6bfca')
        self.c7f3.config(text='0', bg='#b6bfca')
        self.c7f4.config(text='-', bg='#b6bfca')

        self.c8f1.config(text='0', bg='#b6bfca')
        self.c8f2.config(text='0', bg='#b6bfca')
        self.c8f3.config(text='0', bg='#b6bfca')
        self.c8f4.config(text='-', bg='#b6bfca')

        self.c9f1.config(text='0', bg='#b6bfca')
        self.c9f2.config(text='0', bg='#b6bfca')
        self.c9f3.config(text='0', bg='#b6bfca')
        self.c9f4.config(text='-', bg='#b6bfca')

        self.c10f1.config(text='0', bg='#b6bfca')
        self.c10f2.config(text='0', bg='#b6bfca')
        self.c10f3.config(text='0', bg='#b6bfca')
        self.c10f4.config(text='-', bg='#b6bfca')

        self.c11f1.config(text='B', bg='#b6bfca')
        self.c11f2.config(text='B', bg='#b6bfca')
        self.c11f3.config(text='B', bg='#b6bfca')
        self.c11f4.config(text='-', bg='#b6bfca')

    def actualizar(self, pool):
        for listado in pool:
            self.generar(listado)

    def generar(self, listado):
        #* Etiquetas de salida: Primera fila
        self.c1f1.config(text=listado[10][0], bg='#b6bfca')
        self.c1f2.config(text=listado[10][1], bg='#b6bfca')
        self.c1f3.config(text=listado[10][2], bg='#b6bfca')
        self.c1f4.config(text=listado[10][3], bg='#b6bfca')

        #* Segunda fila
        self.c2f1.config(text=listado[9][0], bg='#b6bfca')
        self.c2f2.config(text=listado[9][1], bg='#b6bfca')
        self.c2f3.config(text=listado[9][2], bg='#b6bfca')
        self.c2f4.config(text=listado[9][3], bg='#b6bfca')

        #* Tercera fila
        self.c3f1.config(text=listado[8][0], bg='#b6bfca')
        self.c3f2.config(text=listado[8][1], bg='#b6bfca')
        self.c3f3.config(text=listado[8][2], bg='#b6bfca')
        self.c3f4.config(text=listado[8][3], bg='#b6bfca')

        #* Cuarta fila
        self.c4f1.config(text=listado[7][0], bg='#b6bfca')
        self.c4f2.config(text=listado[7][1], bg='#b6bfca')
        self.c4f3.config(text=listado[7][2], bg='#b6bfca')
        self.c4f4.config(text=listado[7][3], bg='#b6bfca')
        #* Quinta fila
        self.c5f1.config(text=listado[6][0], bg='#b6bfca')
        self.c5f2.config(text=listado[6][1], bg='#b6bfca')
        self.c5f3.config(text=listado[6][2], bg='#b6bfca')
        self.c5f4.config(text=listado[6][3], bg='#b6bfca')

        #* Sexta fila
        self.c6f1.config(text=listado[5][0], bg='#b6bfca')
        self.c6f2.config(text=listado[5][1], bg='#b6bfca')
        self.c6f3.config(text=listado[5][2], bg='#b6bfca')
        self.c6f4.config(text=listado[5][3], bg='#b6bfca')

        #* Séptima fila
        self.c7f1.config(text=listado[4][0], bg='#b6bfca')
        self.c7f2.config(text=listado[4][1], bg='#b6bfca')
        self.c7f3.config(text=listado[4][2], bg='#b6bfca')
        self.c7f4.config(text=listado[4][3], bg='#b6bfca')

        #* Octava fila
        self.c8f1.config(text=listado[3][0], bg='#b6bfca')
        self.c8f2.config(text=listado[3][1], bg='#b6bfca')
        self.c8f3.config(text=listado[3][2], bg='#b6bfca')
        self.c8f4.config(text=listado[3][3], bg='#b6bfca')

        #* Novena fila
        self.c9f1.config(text=listado[2][0], bg='#b6bfca')
        self.c9f2.config(text=listado[2][1], bg='#b6bfca')
        self.c9f3.config(text=listado[2][2], bg='#b6bfca')
        self.c9f4.config(text=listado[2][3], bg='#b6bfca')

        #* Décima fila
        self.c10f1.config(text=listado[1][0], bg='#b6bfca')
        self.c10f2.config(text=listado[1][1], bg='#b6bfca')
        self.c10f3.config(text=listado[1][2], bg='#b6bfca')
        self.c10f4.config(text=listado[1][3], bg='#b6bfca')

        #* Undécima fila
        self.c11f1.config(text=listado[0][0], bg='#b6bfca')
        self.c11f2.config(text=listado[0][1], bg='#b6bfca')
        self.c11f3.config(text=listado[0][2], bg='#b6bfca')
        self.c11f4.config(text=listado[0][3], bg='#b6bfca')
        self.mainwindow.update()
        time.sleep(2.2)

if __name__ == '__main__':
    Interfaz().ventana()