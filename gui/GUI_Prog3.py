from tkinter import Tk,Label,PhotoImage
root =Tk()
photo = PhotoImage(file="Eagle.gif")
Eagle = Label(master=root, image=photo)
Eagle.pack()
root.mainloop()
