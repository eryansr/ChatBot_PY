from tkinter import Tk, Frame, Label, PhotoImage
import tkinter as tk
from PIL import Image

raiz=tk.Tk()

#raiz del codigo
raiz.title("WildBot")
raiz.config(bg="black")
raiz.iconbitmap("3.ico")
raiz.geometry("600x400")

frame1=Frame() #primer frame
frame1.pack(fill="y", expand="true")
frame1.config(bg="black")
frame1.config(width="500", height="400")

#gif decodificacion
file="media/13.gif"

info = Image.open(file)

frames = info.n_frames  

im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

count = 0
anim = None
def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = frame1.after(50,lambda :animation(count))

def stop_animation():
    frame1.after_cancel(anim)

#Titulo
label= tk.Label(frame1, text="Machin troll", fg="red", font=(46), cursor="pirate", bg="black")
label.place(x=10, y=20)
label.pack()

#Frame Animacion
gif_label = tk.Label(frame1,image="", cursor="pirate")
gif_label.pack()
gif_label.config(bg="black")

#Boton inicio
start = tk.Button(frame1,text="start",command=lambda :animation(count))
start.pack()

#Boton Final
stop = tk.Button(frame1,text="stop",command=stop_animation)
stop.pack()

raiz.mainloop() 