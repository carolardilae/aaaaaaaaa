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
        self.draw()

    def draw(self):
        # Dibujar el rectángulo
        self.rectangulo = self.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill="blue")
        
        # Coordenadas para la línea roja
        self.draw_lineas()

    def draw_lineas(self):
        # Coordenadas para la línea roja
        x1 = self.x + self.width / 2
        y1 = self.y - 50
        x2 = self.x + self.width / 2
        y2 = self.y
        
        # Dibujar o actualizar la línea roja
        if self.linea_roja is None:
            self.linea_roja = self.canvas.create_line(x1, y1, x2, y2, fill="red", width=5)
        else:
            self.canvas.coords(self.linea_roja, x1, y1, x2, y2)
        
        # Coordenadas para la línea rosada (un poco más arriba que la línea roja)
        y1_rosada = y1 - 50  # Ajusta este valor para la altura de la línea rosada por encima de la línea roja
        y2_rosada = y2 - 50
        
        # Dibujar o actualizar la línea rosada encima de la línea roja
        if self.linea_rosada is None:
            self.linea_rosada = self.canvas.create_line(x1, y1_rosada, x2, y2_rosada, fill="pink", width=5)
        else:
            self.canvas.coords(self.linea_rosada, x1, y1_rosada, x2, y2_rosada)

    def move(self, dx, dy):
        # Mover el rectángulo
        self.canvas.move(self.rectangulo, dx, dy)
        self.x += dx
        self.y += dy
        
        # Actualizar la posición de las líneas
        self.draw_lineas()

    def move_linea_roja_45_grados(self):
        # Coordenadas del centro del rectángulo
        center_x = self.x + self.width / 2
        center_y = self.y

        # Longitud de la línea roja
        line_length = 50

        # Coordenadas finales de la línea roja a 45 grados
        x1_roja = center_x
        y1_roja = center_y
        x2_roja = center_x + line_length * math.cos(math.radians(45))
        y2_roja = center_y + line_length * math.sin(math.radians(45))

        # Actualizar la línea roja a 45 grados
        self.canvas.coords(self.linea_roja, x1_roja, y1_roja, x2_roja, y2_roja)

        # Coordenadas para la línea rosada a 90 grados respecto a la línea roja
        x1_rosada = x2_roja
        y1_rosada = y2_roja
        x2_rosada = x1_rosada - line_length * math.cos(math.radians(45))
        y2_rosada = y1_rosada + line_length * math.sin(math.radians(45))

        # Actualizar la línea rosada a 90 grados respecto a la línea roja
        self.canvas.coords(self.linea_rosada, x1_rosada, y1_rosada, x2_rosada, y2_rosada)

# Función para mover las figuras
def move_figuras(dx, dy):
    figuras.move(dx, dy)

# Función para mover la línea roja a 45 grados
def move_linea_roja_45_grados():
    figuras.move_linea_roja_45_grados()

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

# Botón para mover la línea roja a 45 grados
button_move_linea_roja = tk.Button(root, text="Mover línea roja a 45 grados", command=move_linea_roja_45_grados)
button_move_linea_roja.pack()

root.mainloop()
