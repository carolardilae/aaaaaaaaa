import tkinter as tk
import math

class CuboBase:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=400, height=400, bg='white')
        self.canvas.pack()

        # Definir las coordenadas del cubo en 3D
        self.cube_vertices = [
            [-50, -50, -50], [50, -50, -50], [50, 50, -50], [-50, 50, -50],  # Trasera
            [-50, -50, 50], [50, -50, 50], [50, 50, 50], [-50, 50, 50]       # Delantera
        ]

        # Definir las caras del cubo (conexiones entre los vértices) y sus colores
        self.cube_faces = [
            (0, 1, 2, 3, 'black'),   # Cara trasera
            (4, 5, 6, 7, 'black'),   # Cara delantera
            (0, 1, 5, 4, 'blue'),    # Cara inferior
            (2, 3, 7, 6, 'blue'),    # Cara superior
            (0, 3, 7, 4, 'red'),     # Cara izquierda
            (1, 2, 6, 5, 'pink')     # Cara derecha
        ]

        # Coordenadas del círculo
        self.circle_radius = 20

        # Parámetros de rotación y traslación
        self.angle_y = 0
        self.translation_x = 0

        # Crear los botones
        self.create_buttons()

        # Dibujar el cubo y los círculos inicialmente
        self.update_objects()

    def create_buttons(self):
        boton_izquierda = tk.Button(self.root, text="Izquierda", command=self.mover_izquierda)
        boton_izquierda.pack(side='left', padx=10, pady=10)

        boton_derecha = tk.Button(self.root, text="Derecha", command=self.mover_derecha)
        boton_derecha.pack(side='left', padx=10, pady=10)

        boton_atras = tk.Button(self.root, text="Atrás", command=self.mover_atras)
        boton_atras.pack(side='right', padx=10, pady=10)

        boton_adelante = tk.Button(self.root, text="Adelante", command=self.mover_adelante)
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
        for face in self.cube_faces:
            points = [vertices[vertex][:2] for vertex in face[:-1]]
            color = face[-1]
            self.canvas.create_polygon(points, fill=color, outline='black')

    def draw_circle(self, x, y, color='green'):
        self.canvas.create_oval(x - self.circle_radius, y - self.circle_radius,
                                x + self.circle_radius, y + self.circle_radius,
                                fill=color, outline='black')

    def update_objects(self):
        self.canvas.delete('all')
        projected_vertices = self.project_3d_to_2d(self.cube_vertices)
        self.draw_cube(projected_vertices)
        
        # Círculo verde en la esquina inferior derecha de la cara derecha del cubo
        circle_x1, circle_y1 = projected_vertices[5]
        circle_x1 -= self.circle_radius  # Ajuste para que el círculo esté pegado al cubo
        circle_y1 += self.circle_radius  # Ajuste para que el círculo esté pegado al cubo
        self.draw_circle(circle_x1, circle_y1, color='green')
        
        # Círculo naranja en la esquina inferior izquierda de la cara derecha del cubo
        circle_x2, circle_y2 = projected_vertices[2]
        circle_x2 -= self.circle_radius  # Ajuste para que el círculo esté pegado al cubo
        circle_y2 += self.circle_radius  # Ajuste para que el círculo esté pegado al cubo
        self.draw_circle(circle_x2, circle_y2, color='orange')
        
        # Círculo rojo en la esquina superior derecha de la cara izquierda del cubo
        circle_x3, circle_y3 = projected_vertices[0]
        circle_x3 -= self.circle_radius  # Ajuste para que el círculo esté pegado al cubo
        circle_y3 -= self.circle_radius  # Ajuste para que el círculo esté pegado al cubo
        self.draw_circle(circle_x3, circle_y3, color='red')

        # Círculo azul en la esquina inferior derecha de la cara izquierda del cubo
        circle_x4, circle_y4 = projected_vertices[4]
        circle_x4 -= self.circle_radius  # Ajuste para que el círculo esté pegado al cubo
        circle_y4 += self.circle_radius  # Ajuste para que el círculo esté pegado al cubo
        self.draw_circle(circle_x4, circle_y4, color='blue')

    def mover_izquierda(self):
        self.angle_y -= math.pi / 18  # Rotar 10 grados hacia la izquierda
        self.update_objects()

    def mover_derecha(self):
        self.angle_y += math.pi / 18  # Rotar 10 grados hacia la derecha
        self.update_objects()

    def mover_atras(self):
        self.translation_x -= 10  # Mover 10 unidades hacia atrás (negativo en X)
       
    def mover_adelante(self):
        self.translation_x += 10  # Mover 10 unidades hacia adelante (positivo en X)
        self.update_objects()

# Crear la ventana principal
root = tk.Tk()

# Crear una instancia de CuboBase
cubo = CuboBase(root)

# Iniciar el loop principal de la ventana
root.mainloop()