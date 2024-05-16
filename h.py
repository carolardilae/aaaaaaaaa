import tkinter as tk
import math

class Animation:
    def __init__(self, parent_frame, width=400, height=400):
        self.frame = parent_frame

        self.canvas = tk.Canvas(self.frame, width=width, height=height, bg='white')
        self.canvas.pack()

        self.square = None
        self.circle = None

        self.square_x = 200
        self.circle_x = 235

        self.create_shapes()

    def create_shapes(self):
        # Dibujar el cubo inicialmente en el centro
        cube_vertices = [
            [self.square_x - 10, 190], [self.square_x + 10, 190],
            [self.square_x + 10, 210], [self.square_x - 10, 210]
        ]
        self.square = self.canvas.create_polygon(cube_vertices, fill='red')
        
        # Dibujar la esfera inicialmente al lado derecho del cubo
        self.circle = self.canvas.create_oval(self.circle_x - 10, 190, self.circle_x + 10, 210, fill='blue')

    def move_shapes(self, dx):
        self.canvas.move(self.square, dx, 0)
        self.canvas.move(self.circle, dx, 0)

    def move_right(self):
        self.move_shapes(10)

    def move_left(self):
        self.move_shapes(-10)

class ShapeMoveApp:
    def __init__(self, master):
        self.master = master
        self.animation_frame = tk.Frame(master)
        self.animation_frame.pack()

        # Crear la animación de los objetos
        self.animation = Animation(self.animation_frame)

        # Botón para mover ambos objetos a la derecha
        self.button_right = tk.Button(master, text="Derecha", command=self.animation.move_right)
        self.button_right.pack(side=tk.LEFT)

        # Botón para mover ambos objetos a la izquierda
        self.button_left = tk.Button(master, text="Izquierda", command=self.animation.move_left)
        self.button_left.pack(side=tk.LEFT)

def main():
    root = tk.Tk()
    app = ShapeMoveApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
