import tkinter as tk
import math

class Animacion:
    def __init__(self, root, cube_vertices, cube_faces):
        self.frame = tk.Frame(root)
        self.frame.pack(side="left", padx=10, pady=10)

        self.canvas = tk.Canvas(self.frame, width=400, height=400, bg='white')
        self.canvas.pack()

        # Definir las coordenadas del cubo en 3D
        self.cube_vertices = cube_vertices

        # Definir las caras del cubo (conexiones entre los vértices) y sus colores
        self.cube_faces = cube_faces

        # Parámetros de rotación y traslación
        self.angle_y = 0
        self.translation_x = 0

        # Crear los botones
        self.create_buttons()

        # Dibujar el cubo inicialmente
        self.update_cube()

    def create_buttons(self):
        boton_izquierda = tk.Button(self.frame, text="Izquierda", command=self.mover_izquierda)
        boton_izquierda.pack(side='left', padx=10, pady=10)

        boton_derecha = tk.Button(self.frame, text="Derecha", command=self.mover_derecha)
        boton_derecha.pack(side='left', padx=10, pady=10)

        boton_atras = tk.Button(self.frame, text="Atrás", command=self.mover_atras)
        boton_atras.pack(side='right', padx=10, pady=10)

        boton_adelante = tk.Button(self.frame, text="Adelante", command=self.mover_adelante)
        boton_adelante.pack(side='right', padx=10, pady=10)

    def project_3d_to_2d(self, vertices):
        projected = []
        for x, y, z in vertices:
            # Traslación en el eje X
            x += self.translation_x

            # Rotación alrededor del eje Y
            rotated_x = x * math.cos(self.angle_y) - z * math.sin(self.angle_y)
            rotated_z = x * math.sin(self.angle_y) + z * math.cos(self.angle_y)
            rotated_y = y

            # Proyección simple (sin perspectiva)
            projected.append((200 + rotated_x, 200 + rotated_y))
        return projected

    def draw_cube(self, vertices):
        self.canvas.delete('all')
        for face in self.cube_faces:
            points = [vertices[vertex][:2] for vertex in face[:-1]]
            color = face[-1]
            self.canvas.create_polygon(points, fill=color, outline='black')

    def update_cube(self):
        projected_vertices = self.project_3d_to_2d(self.cube_vertices)
        self.draw_cube(projected_vertices)

    def mover_izquierda(self):
        self.angle_y -= math.pi / 18  # Rotar 10 grados hacia la izquierda
        self.update_cube()

    def mover_derecha(self):
        self.angle_y += math.pi / 18  # Rotar 10 grados hacia la derecha
        self.update_cube()

    def mover_atras(self):
        self.translation_x -= 10  # Mover 10 unidades hacia atrás (negativo en X)
        self.update_cube()

    def mover_adelante(self):
        self.translation_x += 10  # Mover 10 unidades hacia adelante (positivo en X)
        self.update_cube()


# Crear la ventana principal
root = tk.Tk()

# Definir las coordenadas y caras para el cubo base
cube_vertices = [
    [-50, -50, -50], [50, -50, -50], [50, 50, -50], [-50, 50, -50],  # Trasera
    [-50, -50, 50], [50, -50, 50], [50, 50, 50], [-50, 50, 50]       # Delantera
]
cube_faces = [
    (0, 1, 2, 3, 'black'),   # Cara trasera
    (4, 5, 6, 7, 'black'),   # Cara delantera
    (0, 1, 5, 4, 'blue'),    # Cara inferior
    (2, 3, 7, 6, 'blue'),    # Cara superior
    (0, 3, 7, 4, 'red'),     # Cara izquierda
    (1, 2, 6, 5, 'pink')     # Cara derecha
]

# Crear una instancia de Animacion para el cubo base
cubo = Animacion(root, cube_vertices, cube_faces)

# Definir las coordenadas y caras para el brazo uno
brazo_vertices = [
    [-10, -50, -10], [10, -50, -10], [10, 50, -10], [-10, 50, -10],  # Trasera
    [-10, -50, 10], [10, -50, 10], [10, 50, 10], [-10, 50, 10]       # Delantera
]
brazo_faces = [
    (0, 1, 2, 3, 'black'),   # Cara trasera
    (4, 5, 6, 7, 'black'),   # Cara delantera
    (0, 1, 5, 4, 'blue'),    # Cara inferior
    (2, 3, 7, 6, 'blue'),    # Cara superior
    (0, 3, 7, 4, 'red'),     # Cara izquierda
    (1, 2, 6, 5, 'pink')     # Cara derecha
]

# Crear una instancia de Animacion para el brazo uno
brazo_uno = Animacion(root, brazo_vertices, brazo_faces)

# Iniciar el bucle principal
root.mainloop()
