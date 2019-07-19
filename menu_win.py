from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *


def not_done():
    showerror('Not implemented', 'Not yet available')


def make_menu(win):
    top = Menu(win)
    win.config(menu=top)

    file = Menu(top, tearoff=True)
    file.add_command(label='New...', command=not_done, underline=0)
    file.add_command(label='Open...', command=not_done, underline=0)
    file.add_command(label='Quit', command=win.quit, underline=0)
    top.add_cascade(label='File', menu=file, underline=0)

    edit = Menu(top, tearoff=False)
    edit.add_command(label='Cut', command=not_done, underline=0)
    edit.add_command(label='Paste', command=not_done, underline=0)
    edit.add_separator()
    top.add_cascade(label='Edit', menu=edit, underline=0)

    submenu = Menu(edit, tearoff=True)
    submenu.add_command(label='Spam', command=win.quit, underline=0)
    submenu.add_command(label='Eggs', command=not_done, underline=0)
    edit.add_cascade(label='Stuff', menu=submenu, underline=0)


if __name__ == '__main__':
    root = Tk()
    root.title('menu_win')
    make_menu(root)
    msg = Label(root, text='Window menu basics')
    msg.pack(expand=YES, fill=BOTH)
    msg.config(relief=SUNKEN, width=40, height=7, bg='beige')
    root.mainloop()
