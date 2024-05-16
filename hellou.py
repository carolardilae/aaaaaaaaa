from tkinter import *

root = Tk()
marco_principal = Frame()
marco_principal.grid(row=0, column=0)
marco_principal.config(width="500", height="500")
marco_principal.config(bg="pink")
marco_secundario = Frame()
marco_secundario.grid(row=1, column=0)
marco_secundario.config(width="500", height="500")
marco_secundario.config(bg="white")

boton = Button(root, text="jaja lol").grid(row=1, column=1)
#etiqueta = Label(root, text="pene")
#etiqueta.pack()#esto es pa que se ponga
root.mainloop()