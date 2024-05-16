import tkinter as tk
import math

class Animation:
    def __init__(self, parent_frame, vertices, faces, width=400, height=400):
        self.frame = tk.Frame(parent_frame)
        self.frame.pack()

        self.canvas = tk.Canvas(self.frame, width=width, height=height, bg='white')
        self.canvas.pack()

        self.vertices = vertices
        self.faces = faces

        self.angle_y = 0
        self.translation_x = 0

    def project_3d_to_2d(self, vertices):
        projected = []
        for x, y, z in vertices:
            x += self.translation_x
            rotated_x = x * math.cos(self.angle_y) - z * math.sin(self.angle_y)
            rotated_z = x * math.sin(self.angle_y) + z * math.cos(self.angle_y)
            rotated_y = y
            projected.append((self.canvas.winfo_width() / 2 + rotated_x, self.canvas.winfo_height() / 2 + rotated_y))
        return projected

    def draw(self, vertices):
        self.canvas.delete('all')
        for face in self.faces:
            points = [vertices[vertex][:2] for vertex in face[:-1]]
            color = face[-1]
            self.canvas.create_polygon(points, fill=color, outline='black')

    def update(self):
        projected_vertices = self.project_3d_to_2d(self.vertices)
        self.draw(projected_vertices)

    def move_left(self):
        self.angle_y -= math.pi / 18  
        self.update()

    def move_right(self):
        self.angle_y += math.pi / 18  
        self.update()

    def move_back(self):
        self.translation_x -= 10  
        self.update()

    def move_forward(self):
        self.translation_x += 10  
        self.update()

def generate_sphere(radius, num_points):
    vertices = []
    for i in range(num_points):
        phi = math.pi * (i + 0.5) / num_points
        for j in range(num_points):
            theta = 2 * math.pi * j / num_points
            x = radius * math.sin(phi) * math.cos(theta)
            y = radius * math.sin(phi) * math.sin(theta)
            z = radius * math.cos(phi)
            vertices.append([x, y, z])
    return vertices

root = tk.Tk()

# Coordenadas y caras para el cubo
cube_vertices = [
    [-50, -50, -50], [50, -50, -50], [50, 50, -50], [-50, 50, -50],  
    [-50, -50, 50], [50, -50, 50], [50, 50, 50], [-50, 50, 50]       
]
cube_faces = [
    (0, 1, 2, 3, 'black'),   
    (4, 5, 6, 7, 'black'),   
    (0, 1, 5, 4, 'blue'),    
    (2, 3, 7, 6, 'blue'),    
    (0, 3, 7, 4, 'red'),     
    (1, 2, 6, 5, 'pink')     
]

# Coordenadas y caras para la esfera (brazo)
sphere_radius = 50
num_sphere_points = 20
arm_vertices = generate_sphere(sphere_radius, num_sphere_points)
arm_faces = []
for i in range(num_sphere_points - 1):
    for j in range(num_sphere_points - 1):
        v0 = i * num_sphere_points + j
        v1 = v0 + 1
        v2 = (i + 1) * num_sphere_points + j + 1
        v3 = (i + 1) * num_sphere_points + j
        arm_faces.extend([(v0, v1, v2, v3, 'blue')])

# Instancia de la animación para el cubo
cube_animation = Animation(root, cube_vertices, cube_faces)

# Instancia de la animación para el brazo (esfera)
arm_animation = Animation(root, arm_vertices, arm_faces)

# Mover el brazo hacia arriba para superponerlo al cubo
arm_animation.translation_x += 100  

# Crear botones para controlar ambos objetos simultáneamente
left_button = tk.Button(root, text="Izquierda", command=lambda: [cube_animation.move_left(), arm_animation.move_left()])
left_button.pack(side='left', padx=10, pady=10)

right_button = tk.Button(root, text="Derecha", command=lambda: [cube_animation.move_right(), arm_animation.move_right()])
right_button.pack(side='left', padx=10, pady=10)

back_button = tk.Button(root, text="Atrás", command=lambda: [cube_animation.move_back(), arm_animation.move_back()])
back_button.pack(side='right', padx=10, pady=10)

forward_button = tk.Button(root, text="Adelante", command=lambda: [cube_animation.move_forward(), arm_animation.move_forward()])
forward_button.pack(side='right', padx=10, pady=10)

# Agregar las instancias de Animation a la ventana principal
cube_animation.frame.pack(side="left")
arm_animation.frame.pack(side="left")

# Iniciar el bucle principal
root.mainloop()
