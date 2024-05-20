import tkinter as tk

class Figuras:
    def __init__(self, canvas, x, y, width, height):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rectangulo = None
        self.linea_roja = None
        self.linea_rosada = None
        self.draw()

    def draw(self):
        # Dibujar el rectángulo
        self.rectangulo = self.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill="blue")
        
        # Coordenadas para la línea roja
        x1 = self.x + self.width / 2
        y1 = self.y - 50
        x2 = self.x + self.width / 2
        y2 = self.y
        
        # Dibujar la línea roja
        self.linea_roja = self.canvas.create_line(x1, y1, x2, y2, fill="red", width=5)
        
        # Coordenadas para la línea rosada (un poco más arriba que la línea roja)
        y1_rosada = y1 - 50  # Ajusta este valor para la altura de la línea rosada por encima de la línea roja
        y2_rosada = y2 - 50
        
        # Dibujar la línea rosada encima de la línea roja
        self.linea_rosada = self.canvas.create_line(x1, y1_rosada, x2, y2_rosada, fill="pink", width=5)

    def move(self, dx, dy):
        # Mover el rectángulo
        self.canvas.move(self.rectangulo, dx, dy)
        
        # Mover la línea roja
        self.canvas.move(self.linea_roja, dx, dy)
        
        # Mover la línea rosada
        self.canvas.move(self.linea_rosada, dx, dy)

# Función para mover las figuras
def move_figuras(dx, dy):
    figuras.move(dx, dy)

# Configuración de la ventana
root = tk.Tk()
root.title("Figuras con Canvas")

# Creación del lienzo
canvas = tk.Canvas(root, width=800, height=500)
canvas.pack()

# Creación del objeto que representa las figuras
figuras = Figuras(canvas, 200, 100, 100, 50)

# Botones para mover las figuras
button_left = tk.Button(root, text="Mover izquierda", command=lambda: move_figuras(-10, 0))
button_left.pack()

button_right = tk.Button(root, text="Mover derecha", command=lambda: move_figuras(10, 0))
button_right.pack()

root.mainloop()
