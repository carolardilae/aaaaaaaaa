import pandas as pd
import tkinter as tk

class Animacion:
    def __init__(self):
        datos = pd.read_csv('C:/Users/carol/OneDrive/Documentos/datos.data', header=0)
        df = pd.DataFrame(datos)
        self.valorx = df.loc[1, 'x']  # Cambiar a la posición 1
        self.valory = df.loc[1, 'y']  # Cambiar a la posición 1
        self.longitud_del_lado = self.valory  # Longitud del lado del cubo igual a valory

    def __figuras__(self):
        # Calcular las coordenadas de los vértices del cubo en proyección 2D
        vertice_superior_izquierdo_frontal = (self.valorx, self.valory)
        vertice_superior_derecho_frontal = (self.valorx + self.longitud_del_lado, self.valory)
        vertice_inferior_izquierdo_frontal = (self.valorx, self.valory + self.longitud_del_lado)
        vertice_inferior_derecho_frontal = (self.valorx + self.longitud_del_lado, self.valory + self.longitud_del_lado)

        desplazamiento = 50  # Desplazamiento para la proyección en 2D
        vertice_superior_izquierdo_trasero = (self.valorx + desplazamiento, self.valory - desplazamiento)
        vertice_superior_derecho_trasero = (self.valorx + self.longitud_del_lado + desplazamiento, self.valory - desplazamiento)
        vertice_inferior_izquierdo_trasero = (self.valorx + desplazamiento, self.valory + self.longitud_del_lado - desplazamiento)
        vertice_inferior_derecho_trasero = (self.valorx + self.longitud_del_lado + desplazamiento, self.valory + self.longitud_del_lado - desplazamiento)

        # Calcular el tamaño del lienzo
        canvas_width = self.valorx + self.longitud_del_lado + desplazamiento + 20  # Añadir un espacio adicional de 20 píxeles
        canvas_height = self.valory + self.longitud_del_lado + desplazamiento + 20  # Añadir un espacio adicional de 20 píxeles

        # Crear la ventana y el lienzo con el tamaño calculado
        root = tk.Tk()
        canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
        canvas.pack()

        # Dibujar las líneas del cubo
        self.lineas = []
        # Caras frontal
        self.lineas.append(canvas.create_line(*vertice_superior_izquierdo_frontal, *vertice_superior_derecho_frontal, fill='red'))
        self.lineas.append(canvas.create_line(*vertice_superior_derecho_frontal, *vertice_inferior_derecho_frontal, fill='green'))
        self.lineas.append(canvas.create_line(*vertice_inferior_derecho_frontal, *vertice_inferior_izquierdo_frontal, fill='blue'))
        self.lineas.append(canvas.create_line(*vertice_inferior_izquierdo_frontal, *vertice_superior_izquierdo_frontal, fill='purple'))
        
        # Caras trasera
        self.lineas.append(canvas.create_line(*vertice_superior_izquierdo_trasero, *vertice_superior_derecho_trasero, fill='red'))
        self.lineas.append(canvas.create_line(*vertice_superior_derecho_trasero, *vertice_inferior_derecho_trasero, fill='green'))
        self.lineas.append(canvas.create_line(*vertice_inferior_derecho_trasero, *vertice_inferior_izquierdo_trasero, fill='blue'))
        self.lineas.append(canvas.create_line(*vertice_inferior_izquierdo_trasero, *vertice_superior_izquierdo_trasero, fill='purple'))
        
        # Aristas que conectan las caras frontal y trasera
        self.lineas.append(canvas.create_line(*vertice_superior_izquierdo_frontal, *vertice_superior_izquierdo_trasero, fill='black'))
        self.lineas.append(canvas.create_line(*vertice_superior_derecho_frontal, *vertice_superior_derecho_trasero, fill='black'))
        self.lineas.append(canvas.create_line(*vertice_inferior_izquierdo_frontal, *vertice_inferior_izquierdo_trasero, fill='black'))
        self.lineas.append(canvas.create_line(*vertice_inferior_derecho_frontal, *vertice_inferior_derecho_trasero, fill='black'))

        # Función para mover el cubo hacia la derecha
        def mover_derecha():
            for linea in self.lineas:
                canvas.move(linea, 10, 0)  # Mover cada línea 10 píxeles a la derecha

        # Función para mover el cubo hacia la izquierda
        def mover_izquierda():
            for linea in self.lineas:
                canvas.move(linea, -10, 0)  # Mover cada línea 10 píxeles a la izquierda

        # Botón para mover el cubo hacia la derecha
        btn_mover_derecha = tk.Button(root, text="Mover Derecha", command=mover_derecha)
        btn_mover_derecha.pack()

        # Botón para mover el cubo hacia la izquierda
        btn_mover_izquierda = tk.Button(root, text="Mover Izquierda", command=mover_izquierda)
        btn_mover_izquierda.pack()

# Crear una instancia de la clase Animacion
el_pepe = Animacion()

# Llamar al método __figuras__
el_pepe.__figuras__()

# Ejecutar la aplicación
tk.mainloop()
