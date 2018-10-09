from tkinter import Tk, Label,RAISED,LEFT,RIGHT,TOP,BOTTOM
root =Tk()
hello = Label(master = root,background='green',padx=12,pady=20,foreground='blue', relief=RAISED,borderwidth=12 ,text="Hello Moto")
hello1 = Label(master = root,background='green',padx=12,pady=20,foreground='blue', relief=RAISED,borderwidth=12 ,text="Hello Moto")

#hello.pack(side=BOTTOM)
hello1.pack(expand=True)
root.mainloop()
