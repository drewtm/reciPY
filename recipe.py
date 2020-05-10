from tkinter import *
from recipe_data import ITEM, COLOR
import tkinter.font as tkFont
#import tkfont

itemID=[]
itemMenu=[]
numMenu=[]
remButton=[]

class makethefunc:
    def __init__(self, callback, *args, **kwargs):
        self.callback = callback
        self.args = args
        self.kwargs = kwargs

    def __call__(self):
        return self.callback(*self.args, *self.kwargs)

def change_dropdown(*args):
    colormenu.configure(bg=COLOR[thiscolor.get()]["rgb"], activebackground=COLOR[thiscolor.get()]["rgb"])

def remover(lst, n):
    del itemID[n]
    itemMenu[n].destroy()
    del itemMenu[n]
    numMenu[n].destroy()
    del numMenu[n]
    remButton[n].destroy()
    del remButton[n]
    for i in range(n,len(remButton)):
        remButton[i].configure(command=makethefunc(remover, lst, i))

def additem(lst):
    n = len(itemID)
    itemID.append(StringVar(lst))
    itemID[n].set(sorted(ITEM.keys())[0])
    
    itemMenu.append(OptionMenu(lst, itemID[n], *sorted(ITEM.keys())))
    itemMenu[n].grid(column=0)
    
    thisrow = lst.grid_size()[1]-1
    
    numMenu.append(Spinbox(lst, from_=1, to_=10))
    numMenu[n].grid(row=thisrow, column=1)

    remButton.append(Button(lst, text=" - ", command=makethefunc(remover, lst, n)))
    remButton[n].grid(row=thisrow, column=2)

root = Tk()

default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(size=24)
root.option_add("*Font", default_font)

thiscolor = StringVar(root)
thiscolor.set("natural")
colormenu = OptionMenu(root, thiscolor, *sorted(COLOR.keys()))
thiscolor.trace('w', change_dropdown)
colormenu.configure(bg=COLOR[thiscolor.get()]["rgb"], activebackground=COLOR[thiscolor.get()]["rgb"])

itemsframe = Frame(root)
additem(itemsframe)

addbutton = Button(root, text=" + ", command=makethefunc(additem, itemsframe))

recipeframe = Frame(root)
recipe = Text(recipeframe, width=32, height=12)
recipe.grid(sticky=N)

colormenu.grid(sticky=N+E+W)
itemsframe.grid(row=1, sticky=N)
addbutton.grid(row=2, sticky=NE)
recipeframe.grid(row=0, column=1, rowspan=3)

mainloop()