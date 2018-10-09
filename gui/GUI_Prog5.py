from tkinter import Tk,Button,Label
from tkinter.messagebox import showinfo
from time import localtime,strftime,gmtime
root =Tk()
def greenwich():
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n',gmtime())
    print("GreenWichTime\n"+"="+time)
def local():
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n',localtime())
    print("LocalTime\n"+"="+time)
buttonl = Button(root, text="Click It!",command=local)
buttong = Button(root, text="Click It!",command=greenwich)
buttonl.pack()
buttong.pack()
root.mainloop()
