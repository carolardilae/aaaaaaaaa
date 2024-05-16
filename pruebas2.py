import tkinter as tk
import math

class RectanguloLinea:
    def __init__(self, canvas, size):
        self.canvas = canvas
        self.size = size
        self.angle = 0
        self.draw()

    def draw(self):
        self.canvas.delete("rectangulo_linea")
        
        # Dibujar el rectángulo
        rect_x1 = 100 - self.size / 2
        rect_y1 = 150 - self.size / 4
        rect_x2 = 100 + self.size / 2
        rect_y2 = 150 + self.size / 4
        rotated_rect_x1, rotated_rect_y1 = self.rotate_point(rect_x1, rect_y1, self.angle)
        rotated_rect_x2, rotated_rect_y2 = self.rotate_point(rect_x2, rect_y2, self.angle)
        self.canvas.create_rectangle(rotated_rect_x1, rotated_rect_y1, rotated_rect_x2, rotated_rect_y2, fill="blue", tags="rectangulo_linea")
        
        # Dibujar la línea
        line_x1 = 100
        line_y1 = 150 - self.size / 4
        line_x2 = 100
        line_y2 = 50
        rotated_line_x1, rotated_line_y1 = self.rotate_point(line_x1, line_y1, self.angle)
        rotated_line_x2, rotated_line_y2 = self.rotate_point(line_x2, line_y2, self.angle)
        self.canvas.create_line(rotated_line_x1, rotated_line_y1, rotated_line_x2, rotated_line_y2, fill="red", width=2, tags="rectangulo_linea")

    def rotate_point(self, x, y, angle):
        cx, cy = 100, 150
        angle_rad = math.radians(angle)
        x_new = (x - cx) * math.cos(angle_rad) - (y - cy) * math.sin(angle_rad) + cx
        y_new = (x - cx) * math.sin(angle_rad) + (y - cy) * math.cos(angle_rad) + cy
        return x_new, y_new

    def rotate_rectangulo(self):
        self.angle += 5
        self.draw()

root = tk.Tk()
root.title("Rectángulo y Línea Giratorios")

canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

objeto = RectanguloLinea(canvas, 50)

button_rotate_rectangulo = tk.Button(root, text="Rotar Rectángulo", command=objeto.rotate_rectangulo)
button_rotate_rectangulo.pack()

root.mainloop()
