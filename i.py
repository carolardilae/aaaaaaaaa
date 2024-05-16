import tkinter as tk
import math

class Animation:
    def __init__(self, parent_frame, width=400, height=400):
        self.frame = parent_frame

        self.canvas = tk.Canvas(self.frame, width=width, height=height, bg='white')
        self.canvas.pack()

        self.cube = None
        self.sphere = None

        self.cube_x = 200
        self.sphere_x = 235

        self.create_shapes()

    def create_shapes(self):
        # Dibujar el cubo inicialmente en el centro
        cube_vertices = [
            [self.cube_x - 10, 190, self.cube_x - 10], [self.cube_x + 10, 190, self.cube_x - 10],
            [self.cube_x + 10, 210, self.cube_x - 10], [self.cube_x - 10, 210, self.cube_x - 10],
            [self.cube_x - 10, 190, self.cube_x + 10], [self.cube_x + 10, 190, self.cube_x + 10],
            [self.cube_x + 10, 210, self.cube_x + 10], [self.cube_x - 10, 210, self.cube_x + 10]
        ]
        self.cube = self.draw_cube(cube_vertices)
        
        # Dibujar la esfera inicialmente al lado derecho del cubo
        sphere_radius = 10
        self.sphere = self.canvas.create_oval(self.sphere_x - sphere_radius, 190 - sphere_radius,
                                              self.sphere_x + sphere_radius, 190 + sphere_radius, fill='blue')

    def draw_cube(self, vertices):
        # Dibujar las caras del cubo
        self.canvas.create_polygon(vertices[0][0], vertices[0][1], vertices[1][0], vertices[1][1],
                                    vertices[2][0], vertices[2][1], vertices[3][0], vertices[3][1], fill='red')
        self.canvas.create_polygon(vertices[4][0], vertices[4][1], vertices[5][0], vertices[5][1],
                                    vertices[6][0], vertices[6][1], vertices[7][0], vertices[7][1], fill='red')
        self.canvas.create_polygon(vertices[0][0], vertices[0][1], vertices[1][0], vertices[1][1],
                                    vertices[5][0], vertices[5][1], vertices[4][0], vertices[4][1], fill='red')
        self.canvas.create_polygon(vertices[1][0], vertices[1][1], vertices[2][0], vertices[2][1],
                                    vertices[6][0], vertices[6][1], vertices[5][0], vertices[5][1], fill='red')
        self.canvas.create_polygon(vertices[2][0], vertices[2][1], vertices[3][0], vertices[3][1],
                                    vertices[7][0], vertices[7][1], vertices[6][0], vertices[6][1], fill='red')
        self.canvas.create_polygon(vertices[3][0], vertices[3][1], vertices[0][0], vertices[0][1],
                                    vertices[4][0], vertices[4][1], vertices[7][0], vertices[7][1], fill='red')

    def move_shapes(self, dx):
        self.canvas.move(self.cube, dx, 0)
        self.canvas.move(self.sphere, dx, 0)

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
