import tkinter as tk
from maquina_de_turing import maquina

def evaluar():
    # Obtener el contenido de las cajas de texto
    texto1 = entrada1.get()
    texto2 = entrada2.get()

    # Realizar alguna operación o evaluación con los textos

    # Mostrar el resultado en el área de texto
    resultado.config(state="normal")
    resultado.delete("1.0", "end")
    resultado.insert("end", "Resultado: {}".format(texto1 + texto2))
    resultado.config(state="disabled")
def evaluar1():
    m = maquina()
    a = entrada1.get()
    b = entrada2.get()
    m.turing(a,b)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana de ejemplo")

# Crear los labels
label1 = tk.Label(ventana, text="Texto 1:")
label1.pack()

# Crear la caja de texto 1
entrada1 = tk.Entry(ventana)
entrada1.pack()

label2 = tk.Label(ventana, text="Texto 2:")
label2.pack()

# Crear la caja de texto 2
entrada2 = tk.Entry(ventana)
entrada2.pack()

# Crear el área de texto
resultado = tk.Text(ventana, height=10, width=30)
resultado.config(state="disabled")
resultado.pack()

# Crear el botón
boton = tk.Button(ventana, text="Evaluar", command=evaluar1)
boton.pack()

# Iniciar el bucle de eventos
ventana.mainloop()


    