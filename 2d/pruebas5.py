import tkinter as tk
import math

class Figuras:
    def __init__(self, canvas, x, y, width, height):
        self.canvas = canvas
        self.x = x
        self.y = y + 100  # Ajuste de la posición vertical
        self.width = width
        self.height = height
        self.rectangulo = None
        self.linea_roja = None
        self.linea_rosada = None
        self.angle = 90  # Angle in degrees, initially 90 (vertical)
        self.draw()

    def draw(self):
        # Dibujar el rectángulo
        self.rectangulo = self.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill="blue")
        # Dibujar las líneas
        self.draw_lineas()

    def draw_lineas(self):
        # Centro del rectángulo
        center_x = self.x + self.width / 2
        center_y = self.y

        # Longitud de las líneas
        line_length = 50

        # Coordenadas para la línea roja
        x1_roja = center_x
        y1_roja = center_y
        x2_roja = center_x + line_length * math.cos(math.radians(self.angle))
        y2_roja = center_y + line_length * math.sin(math.radians(self.angle))

        # Dibujar o actualizar la línea roja
        if self.linea_roja is None:
            self.linea_roja = self.canvas.create_line(x1_roja, y1_roja, x2_roja, y2_roja, fill="red", width=5)
        else:
            self.canvas.coords(self.linea_roja, x1_roja, y1_roja, x2_roja, y2_roja)

        # Coordenadas para la línea rosada (90 grados respecto a la línea roja)
        x1_rosada = x2_roja
        y1_rosada = y2_roja
        x2_rosada = x1_rosada - line_length * math.sin(math.radians(self.angle))
        y2_rosada = y1_rosada + line_length * math.cos(math.radians(self.angle))

        # Dibujar o actualizar la línea rosada
        if self.linea_rosada is None:
            self.linea_rosada = self.canvas.create_line(x1_rosada, y1_rosada, x2_rosada, y2_rosada, fill="pink", width=5)
        else:
            self.canvas.coords(self.linea_rosada, x1_rosada, y1_rosada, x2_rosada, y2_rosada)

    def move(self, dx, dy):
        # Mover el rectángulo
        self.canvas.move(self.rectangulo, dx, dy)
        self.x += dx
        self.y += dy
        
        # Actualizar la posición de las líneas
        self.draw_lineas()

    def set_angle(self, angle):
        # Cambiar el ángulo de la línea roja
        self.angle = angle
        # Redibujar las líneas con el nuevo ángulo
        self.draw_lineas()

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

# Botones para mover la línea roja a diferentes ángulos
button_move_linea_45 = tk.Button(root, text="Mover línea roja a 45 grados", command=lambda: figuras.set_angle(45))
button_move_linea_45.pack()

button_move_linea_300 = tk.Button(root, text="Mover línea roja a 300 grados", command=lambda: figuras.set_angle(300))
button_move_linea_300.pack()

button_move_linea_225 = tk.Button(root, text="Mover línea roja a 225 grados", command=lambda: figuras.set_angle(225))
button_move_linea_225.pack()

button_move_linea_200 = tk.Button(root, text="Mover línea roja a 200 grados", command=lambda: figuras.set_angle(200))
button_move_linea_200.pack()

button_move_linea_180 = tk.Button(root, text="Mover línea roja a 180 grados", command=lambda: figuras.set_angle(180))
button_move_linea_180.pack()

root.mainloop()
