from tkinter import *
import sys
from bson.json_util import dumps

class Display(Frame):
    def __init__(self, parent=0):
        Frame.__init__(self, parent)
        self.entry = Entry(self)
        self.entry.pack()
        self.doIt = Button(self, text="DoIt", command=self.onEnter)
        self.doIt.pack()
        self.output = Text(self)
        self.output.pack()
        sys.stdout = self
        self.pack()

    def onEnter(self):
        eval()

    def write(self, txt):
        self.output.insert(END, str(txt))


if __name__ == '__main__':
    Display().mainloop()
