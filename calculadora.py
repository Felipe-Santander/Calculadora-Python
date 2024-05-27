import tkinter as tk

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Variable para almacenar la entrada de la calculadora
entrada = tk.StringVar()

# Función para actualizar la entrada
def presionar_tecla(tecla):
    entrada.set(entrada.get() + tecla)

# Función para calcular el resultado
def calcular():
    try:
        resultado = str(eval(entrada.get()))
        entrada.set(resultado)
    except Exception as e:
        entrada.set("Error")

# Función para limpiar la entrada
def limpiar():
    entrada.set("")

# Configuración de la pantalla de la calculadora
pantalla = tk.Entry(ventana, textvariable=entrada, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
pantalla.grid(row=0, column=0, columnspan=4)

# Botones de la calculadora
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Añadir botones a la interfaz
for (texto, fila, columna) in botones:
    if texto == '=':
        boton = tk.Button(ventana, text=texto, padx=20, pady=20, font=("Arial", 18), command=calcular)
    else:
        boton = tk.Button(ventana, text=texto, padx=20, pady=20, font=("Arial", 18), command=lambda t=texto: presionar_tecla(t))
    boton.grid(row=fila, column=columna)

# Botón de limpiar
boton_limpiar = tk.Button(ventana, text='Borrar', padx=20, pady=20, font=("Arial", 18), command=limpiar)
boton_limpiar.grid(row=5, column=0, columnspan=4)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
