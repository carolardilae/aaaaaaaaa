import tkinter as tk

class ShapeMoveApp:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()
        
        # Dibujar el cuadrado inicialmente en el centro
        self.square = self.canvas.create_rectangle(190, 190, 210, 210, fill='red')
        
        # Dibujar el círculo inicialmente al lado derecho del cuadrado
        self.circle = self.canvas.create_oval(225, 190, 245, 210, fill='blue')
        
        # Botón para mover ambos objetos a la derecha
        self.button_right = tk.Button(master, text="Derecha", command=self.move_right)
        self.button_right.pack(side=tk.LEFT)
        
        # Botón para mover ambos objetos a la izquierda
        self.button_left = tk.Button(master, text="Izquierda", command=self.move_left)
        self.button_left.pack(side=tk.LEFT)
    
    def move_right(self):
        self.canvas.move(self.square, 10, 0)
        self.canvas.move(self.circle, 10, 0)
    
    def move_left(self):
        self.canvas.move(self.square, -10, 0)
        self.canvas.move(self.circle, -10, 0)

def main():
    root = tk.Tk()
    app = ShapeMoveApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
