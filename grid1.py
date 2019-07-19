from tkinter import *

colors = ['red', 'green', 'orange', 'white', 'yellow', 'blue']

frame0 = Frame()
Label(frame0, text='Grid').grid(columnspan=2)


frame1 = Frame()
r = 0
for c in colors:
    label = Label(frame1, text=c, relief=RIDGE, width=25)
    ent = Entry(frame1, bg=c, relief=SUNKEN, width=50)
    ent.insert(0, 'color: ' + c)
    label.grid(row=r, column=0, sticky=NSEW)
    ent.grid(row=r, column=1, sticky=NSEW)
    r += 1
frame1.columnconfigure(0, weight=1)
frame1.rowconfigure(0, weight=1)
frame1.rowconfigure(2, weight=1)
frame1.columnconfigure(1, weight=1)

frame2 = Frame()
for (row, color) in enumerate(colors):
    Label(frame2, text=color, relief=RIDGE, width=25).grid(row=row, column=0)
    ent1 = Entry(frame2, bg=color, relief=SUNKEN, width=50)
    ent1.insert(0, 'color: ' + color)
    ent1.grid(row=row, column=1)

frame3 = Frame()
for color in colors:
    rowframe = Frame(frame3)
    label = Label(rowframe, text=color, relief=RIDGE, width=25)
    ent = Entry(rowframe, bg=color, relief=SUNKEN, width=50)
    ent.insert(0, 'color: ' + color)

    rowframe.pack(side=TOP)
    label.pack(side=LEFT)
    ent.pack(side=RIGHT)


frame0.pack(ipady=10)
frame1.pack(ipady=10)
frame2.pack(ipady=10)
frame3.pack()
mainloop()
