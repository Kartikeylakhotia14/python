from tkinter import Tk,Button,Label,Entry,END
from time import strptime,strftime
from tkinter.messagebox import showinfo
def compute():
    global dateEnd
    date=dateEnd.get()
    weekday = strftime('%A', strptime(date, '%b %d, %Y'))
    showinfo(message = '{} was a {}'.format(date, weekday))
    dateEnd.delete(0,END)
root=Tk()
text =Label(root, text="Enter Date")
text.grid(row =0,column=0)
dateEnd=Entry(root)
dateEnd.grid(row=0,column=1)
button=Button(root,text="Find",command=compute)
button.grid(row=1,column=0,columnspan=2)
