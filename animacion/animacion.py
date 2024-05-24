import pandas as pd
import tkinter as tk 

class Animacion:
    def __init__(self):
        datos = pd.read_csv('C:/Users/carol/OneDrive/Documentos/datos.data', header=0)
        df = pd.DataFrame(datos)
        self.valorx = df.loc[2, 'x']  # Cambiar a la posición 1
        self.valory = df.loc[2, 'y']  # Cambiar a la posición 1
        self.longitud_del_lado = self.valory  # Longitud del lado del cuadrado igual a valory

    def __figuras__(self):
        # Calcular las coordenadas de los vértices del cuadrado
        vertice_superior_izquierdo = (self.valorx, self.valory)
        vertice_superior_derecho = (self.valorx + self.longitud_del_lado, self.valory)
        vertice_inferior_izquierdo = (self.valorx, self.valory + self.longitud_del_lado)
        vertice_inferior_derecho = (self.valorx + self.longitud_del_lado, self.valory + self.longitud_del_lado)
        
        # Calcular el tamaño del lienzo
        canvas_width = self.valorx + self.longitud_del_lado + 20  # Añadir un espacio adicional de 20 píxeles
        canvas_height = self.valory + self.longitud_del_lado + 20  # Añadir un espacio adicional de 20 píxeles
        
        # Crear la ventana y el lienzo con el tamaño calculado
        root = tk.Tk()
        canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
        canvas.pack()
        
        # Dibujar las líneas del cuadrado
        self.lineas = []
        self.lineas.append(canvas.create_line(*vertice_superior_izquierdo, *vertice_superior_derecho, fill='red'))
        self.lineas.append(canvas.create_line(*vertice_superior_derecho, *vertice_inferior_derecho, fill='green'))
        self.lineas.append(canvas.create_line(*vertice_inferior_derecho, *vertice_inferior_izquierdo, fill='blue'))
        self.lineas.append(canvas.create_line(*vertice_inferior_izquierdo, *vertice_superior_izquierdo, fill='purple'))

        # Calcular las coordenadas de la línea adicional (90 grados respecto a la línea roja)
        x_centro_linea = (self.valorx + self.valorx + self.longitud_del_lado) // 2  # Centro en el eje x de la línea roja
        y_centro_linea = self.valory - 50  # Valor específico para el valory de la nueva línea
        
        # Dibujar la línea adicional
        linea_adicional = canvas.create_line(x_centro_linea, y_centro_linea, x_centro_linea, self.valory, fill='black')
        self.lineas.append(linea_adicional)

        # Función para mover el cuadrado hacia la derecha
        def mover_derecha():
            for linea in self.lineas:
                canvas.move(linea, 10, 0)  # Mover cada línea 10 píxeles a la derecha
        
        # Función para mover el cuadrado hacia la izquierda
        def mover_izquierda():
            for linea in self.lineas:
                canvas.move(linea, -10, 0)  # Mover cada línea 10 píxeles a la izquierda

        # Botón para mover el cuadrado hacia la derecha
        btn_mover_derecha = tk.Button(root, text="Mover Derecha", command=mover_derecha)
        btn_mover_derecha.pack()

        # Botón para mover el cuadrado hacia la izquierda
        btn_mover_izquierda = tk.Button(root, text="Mover Izquierda", command=mover_izquierda)
        btn_mover_izquierda.pack()

# Crear una instancia de la clase Animacion
el_pepe = Animacion()

# Llamar al método __figuras__
el_pepe.__figuras__()

# Ejecutar la aplicación
tk.mainloop()
