import tkinter as tk

root = tk.Tk()

# Crear un lienzo para dibujar
canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack()

# Dibujar un rectángulo rojo en el lienzo
canvas.create_rectangle(100, 100, 300, 300, fill='red')

# Crear botones para controlar la posición del rectángulo
left_button = tk.Button(root, text="Izquierda")
left_button.pack(side='left', padx=10, pady=10)

right_button = tk.Button(root, text="Derecha")
right_button.pack(side='left', padx=10, pady=10)

root.mainloop()
