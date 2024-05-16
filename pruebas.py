import tkinter as tk

class Figuras:
    def __init__(self, canvas, x, y, width, height):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rectangulo = None
        self.linea = None
        self.draw()

    def draw(self):
        # Dibujar el rectángulo
        self.rectangulo = self.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill="blue")
        
        # Dibujar la línea encima del rectángulo
        x1 = self.x + self.width /2
        y1 = self.y - 50
        x2 = self.x + self.width /2
        y2 = self.y
        self.linea = self.canvas.create_line(x1, y1, x2, y2, fill="red", width=5)

    def move(self, dx, dy):
        # Mover el rectángulo
        self.canvas.move(self.rectangulo, dx, dy)
        
        # Mover la línea
        self.canvas.move(self.linea, dx, dy)

# Función para mover las figuras
def move_figuras(dx, dy):
    figuras.move(dx, dy)

# Configuración de la ventana
root = tk.Tk()
root.title("Figuras con Canvas")

# Creación del lienzo
canvas = tk.Canvas(root, width=600, height=250)
canvas.pack()

# Creación del objeto que representa las figuras
figuras = Figuras(canvas, 200, 100, 100, 50)

# Botones para mover las figuras
button_up = tk.Button(root, text="Mover izquierda", command=lambda: move_figuras(-10, 0))
button_up.pack()

button_down = tk.Button(root, text="Mover derecha", command=lambda: move_figuras(10, 0))
button_down.pack()

root.mainloop()
