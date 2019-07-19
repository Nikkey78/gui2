"""простой настраиваемый компонент окна списка с прокруткой"""
from tkinter import *
from tkinter import ttk


class ScrolledList(Frame):
    def __init__(self, options, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.make_widgets(options)

    def make_widgets(self, options):
        sbar = ttk.Scrollbar(self)
        list = Listbox(self, relief=SUNKEN)

        sbar.config(command=list.yview)             # вызвать list.yview при перемещении
        list.config(yscrollcommand=sbar.set)        # вызвать sbar.set при перемещении

        sbar.pack(side=RIGHT, fill=Y)
        list.pack(side=LEFT, expand=YES, fill=BOTH)
        pos = 0
        for label in options:
            # list.insert(pos, label)
            # pos += 1
        # another variant
            list.insert(END, label)

        list.config(selectmode=SINGLE, setgrid=1)
        list.bind('<Double-1>', self.handle_list)
        self.listbox = list

    def handle_list(self, event):
        index = self.listbox.curselection()
        label = self.listbox.get(index)
        self.run_command(label)

    def run_command(self, selection):
        print('You selected:', selection)


if __name__ == '__main__':
    options = (('Lumberjack-%s' % x) for x in range(20))
    ScrolledList(options).mainloop()
