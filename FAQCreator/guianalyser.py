from tkinter import *
class scrollTxtArea:
    global kathi
    
    def __init__(self, root):
        frame = Frame(root)
        frame.pack()
        self.textPad(frame)
        self.createEntry(frame)
        self.createButton(frame)
        self.textArea(frame)
        return
    def textPad(self,frame):
        textPad = Frame(frame)
        self.text = Text(textPad, height=8, width=90)
              
        scroll = Scrollbar(textPad)
        self.text.configure(yscrollcommand=scroll.set)

        self.text.pack(side=LEFT)
        scroll.pack(side=RIGHT,fill=Y)
        textPad.pack(side=TOP)
        self.text.get("1.0",END)
        return
    def textArea(self,frame):
        textArea = Frame(frame)
        self.textResult = Text(textArea, height=8, width=90)
        scroll = Scrollbar(textArea)
        self.textResult.configure(yscrollcommand=scroll.set)
        self.textResult.pack(side=LEFT)
        scroll.pack(side=RIGHT, fill=Y)
        textArea.pack(side=TOP)
        self.textResult.get("1.0", END)
        
    def createEntry(self,frame):
        entryBox = Frame(frame)
        self.entry = Entry(entryBox)
        self.entry.pack(side=LEFT)
        entryBox.pack(side=TOP)
        return
    
    def createButton(self,frame):
        button = Frame(frame)
        self.button = Button(button, text="Print",command=self.printValue)
        self.button.pack(side=LEFT)
        button.pack(side=TOP)
        return

    def printValue(self):
        self.textResult.insert(END,"\n"+self.entry.get())
        print(self.entry.get())
        print(self.text.get("1.0",END).split("\n")[0])
        
def main():
    root = Tk()
    root.resizable(width=False, height=False)
    foo = scrollTxtArea(root)
    root.title('Text with Scroll')
    root.mainloop()
    return foo


