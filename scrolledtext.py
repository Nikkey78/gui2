"""простой компонент просмотра текста или содержимого файла"""
from tkinter import *
from tkinter import ttk

print('PP4E scrolledtext')


class ScrolledText(Frame):
    def __init__(self, parent=None, text='', file=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.make_widgets()
        self.set_text(text, file)

    def make_widgets(self):
        sbar = ttk.Scrollbar(self)
        text = Text(self, relief=SUNKEN)

        sbar.config(command=text.yview)
        text.config(yscrollcommand=sbar.set)

        sbar.pack(side=RIGHT, fill=Y)                    # первым добавлен - посл. обрезан
        text.pack(side=LEFT, expand=YES, fill=BOTH)      # Text обрезается первым
        self.text = text

    def set_text(self, text='', file=None):
        if file:
            text = open(file, 'r').read()
            self.text.delete('1.0', END)        # удалить текущий текст
            self.text.insert('1.0', text)       # добавить в стр. 1, кол. 0
            self.text.mark_set(INSERT, '1.0')   # установить курсор вставки
            self.text.focus()                   # сэкономить щелчок мышью

    def get_text(self):
        return self.text.get('1.0', END+'-1c')  # от начала до конца


if __name__ == '__main__':
    root = Tk()
    if len(sys.argv) > 1:
        st = ScrolledText(file=sys.argv[1])  # имя файла в командной строке
    else:
        st = ScrolledText(text='Words\ngo here')  # иначе: две строки

    def show(event):
            print(repr(st.get_text()))  # вывести как простую строку


    root.bind('<Key-Escape>', show)  # esc = выводит дамп текста
    root.mainloop()

