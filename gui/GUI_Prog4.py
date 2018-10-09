from tkinter import Tk,Label,RAISED
root=Tk()
text =[['1','2','3'],
       ['4','5','6'],
       ['7','8','9'],
       ['*','0','#']]
for i in range(4):
    for j in range(3):
        box = Label(root,
                    relief = RAISED,
                    padx=10,
                    pady=12,
                    text=text[i][j])
        box.grid(rowspan=1,row=i,column=j,columnspan=2)
root.mainloop()
