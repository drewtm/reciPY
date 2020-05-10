from tkinter import *
from recipe_data import ITEM, COLOR
import tkinter.font as tkFont
import time

root = Tk()

root.itemID=[]
root.itemMenu=[]
root.numMenu=[]
root.remButton=[]

class makethefunc:
    def __init__(self, callback, *args, **kwargs):
        self.callback = callback
        self.args = args
        self.kwargs = kwargs

    def __call__(self):
        return self.callback(*self.args, *self.kwargs)

def change_dropdown(*args):
    root.colormenu.configure(bg=COLOR[root.thiscolor.get()]["rgb"], activebackground=COLOR[root.thiscolor.get()]["rgb"])

def remover(lst, n):
    del root.itemID[n]
    root.itemMenu[n].destroy()
    del root.itemMenu[n]
    root.numMenu[n].destroy()
    del root.numMenu[n]
    root.remButton[n].destroy()
    del root.remButton[n]
    for i in range(n,len(root.remButton)):
        root.remButton[i].configure(command=makethefunc(remover, lst, i))

def additem(lst):
    n = len(root.itemID)
    root.itemID.append(StringVar(lst))
    root.itemID[n].set(sorted(ITEM.keys())[0])
    
    root.itemMenu.append(OptionMenu(lst, root.itemID[n], *sorted(ITEM.keys())))
    root.itemMenu[n].grid(column=0)
    
    thisrow = lst.grid_size()[1]-1
    
    root.numMenu.append(Spinbox(lst, from_=1, to_=10))
    root.numMenu[n].grid(row=thisrow, column=1)

    root.remButton.append(Button(lst, text=" - ", command=makethefunc(remover, lst, n)))
    root.remButton[n].grid(row=thisrow, column=2)

def calcAndDraw(R):
    totalweight = sum(int(A.get())*ITEM[B.get()] for A, B in zip(R.numMenu, R.itemID))
    T = R.recipe
    T.config(state=NORMAL)
    T.delete(0.0, END)
    T.insert(0.0, "recipe generated ")
    T.insert(CURRENT,time.asctime())
    T.insert(CURRENT,"\ntotal weight ")
    T.insert(CURRENT, totalweight)
    T.config(state=DISABLED)
    return

default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(size=24)
root.option_add("*Font", default_font)

root.thiscolor = StringVar(root)
root.thiscolor.set("natural")
root.colormenu = OptionMenu(root, root.thiscolor, *sorted(COLOR.keys()))
root.thiscolor.trace('w', change_dropdown)
root.colormenu.configure(bg=COLOR[root.thiscolor.get()]["rgb"], activebackground=COLOR[root.thiscolor.get()]["rgb"])

root.itemsframe = Frame(root)
additem(root.itemsframe)
root.addbutton = Button(root, text=" + ", command=makethefunc(additem, root.itemsframe))

root.recipeframe = Frame(root)
root.recipe = Text(root.recipeframe, width=36, height=12, state=DISABLED)
root.gobutton = Button(root.recipeframe, text="Refresh Recipe", command=makethefunc(calcAndDraw, root))
root.gobutton.grid(sticky=N+E+W)
root.recipe.grid(sticky=N)

root.colormenu.grid(sticky=N+E+W)
root.itemsframe.grid(row=1, sticky=N)
root.addbutton.grid(row=2, sticky=NE)
root.recipeframe.grid(row=0, column=1, rowspan=3)

mainloop()