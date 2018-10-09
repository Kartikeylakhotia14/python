from tkinter import Tk,Canvas
def begin(events):
    global oldx,oldy
    print(events.x)
    print(events.y)
    oldx,oldy=events.x,events.y
def draw(events):
    global oldx,oldy,canvas,ID
    newx,newy=events.x,events.y
    ID.append(canvas.create_line(oldx,oldy,newx,newy))
    oldx,oldy=newx,newy
def delete(events):
    global ID,canvas
    for i in ID:
        canvas.delete(i)
root =Tk()
oldx,oldy=0,0
ID=[]
canvas = Canvas(root,width=100,height=150)
canvas.bind("<Button-1>",begin)
canvas.bind("<Button1-Motion>",draw)
canvas.bind("<Control-Button-1>",delete)
canvas.pack()
root.mainloop()
