import tkinter as tk

ventana = tk.Tk()
ventana.title('Mi primer ventana')
ventana.geometry('600x400+0+0')
ventana.minsize(400,200)
ventana.maxsize(800,600)
ventana.resizable(False,True)

ventana.attributes('-alpha', 0.9)

ventana.iconbitmap('icons/shark.ico')

ventana.configure(bg='lightgreen')

ventana.mainloop()