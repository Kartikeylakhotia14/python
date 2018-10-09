from tkinter import Tk,Text,BOTH

def record(event):
    print(event.keysum_num)
root =Tk()
text = Text(root , width=20,height=5)
text.bind('<KeyPress>',record)
text.pack(expand=True,fill=BOTH)
root.mainloop()
