from tkinter import Tk, Frame, Label, PhotoImage

raiz=Tk()

raiz.title("WildBot")

raiz.config(bg="black")

raiz.iconbitmap("3.ico")

raiz.geometry("600x400")

frame1=Frame()

frame1.pack(fill="y", expand="true")

frame1.config(bg="black")

frame1.config(width="500", height="400")

#frame1.config(cursor="pirate")

#frame1.config(relief="groove")

#frame1.config(bd="35")

label= Label(frame1, text="Machin troll", fg="red", font=(26), cursor="pirate", bg="black")

label.place(x=200, y=20)

#imggif=PhotoImage(file="media/13.gif")
#labelimg= Label(frame1, image=imggif)
#labelimg.place(x=200, y=50)

#segundo frame
#frame2=Frame()
#frame2.pack(side="right", anchor="n")
#frame2.config(bg="green")
#frame2.config(width="200", height="400")

raiz.mainloop() 