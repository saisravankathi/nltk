from tkinter import *
from who import *
import os

class ScrollTxtArea:
    
    def __init__(self, root):
        frame = Frame(root)
        frameG = Frame(root)
        for f in (frame,frameG):
            f.grid(row=0, column=0, sticky="news")
        self.gifFrame(frameG,frame)
        raise_frame(frameG)
        self.textPad(frame)
        self.createEntry(frame)
        self.createButton(frame)
        self.createClearButton(frame)
        self.textArea(frame)
        root.bind_class("Text","<Control-a>",self.selectAllTextAreaText)
        
        
    def textPad(self,frame):
        textPad = Frame(frame)
        self.text = Text(textPad, height=8, width=90)
              
        scroll = Scrollbar(textPad)
        self.text.configure(yscrollcommand=scroll.set)

        self.text.pack(side=LEFT)
        scroll.pack(side=RIGHT,fill=Y)
        textPad.pack(side=TOP)
        self.text.get("1.0",END)
        
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
        self.entry.bind("<Return>", faqEnterPrint)
        self.entry.bind("<Control-a>", self.selectAllText)
        entryBox.pack(side=TOP)
    
    def createButton(self,frame):
        button = Frame(frame)
        self.button = Button(button, text="Print",command=faqPrint)
        self.button.pack(side=LEFT)
        button.pack(side=TOP)
        
    def createClearButton(self,frame):
        clearbutton = Frame(frame)
        self.clrbutton = Button(clearbutton, text="Clear",command=self.clearResults)
        self.clrbutton.pack(side=RIGHT)
        clearbutton.pack(side=TOP)
        
    def getValues(self, clasifier):
        print("before ques: ",self.textResult.index("end-1c"))
        self.textResult.insert(END,"\nQustion:"+foo.entry.get())
        self.textResult.tag_add("question_txt",self.textResult.index("end-1c linestart"),self.textResult.index("end-1c"))
        self.textResult.tag_config("question_txt",foreground="green")
        for v in clasifier.fSet:
            print("before ans: ",self.textResult.index("end-1c"))
            self.textResult.insert(END,"\nAnswer:"+v)
            print("after ans: ",self.textResult.index("end-1c"))
            
    def getAlertValues(self):
        self.textResult.insert(END,"\nWarning: Please enter the question.")

    def clearResults(self):
        self.textResult.delete(1.0,END)
    
    def selectAllText(self,event):
        # select text after 50ms
        root.after(50, self.select_all, event.widget)

    def select_all(self,widget):
        # select text
        widget.select_range(0, 'end')
        # move cursor to the end
        widget.icursor('end')
        
    def selectAllTextAreaText(self, event):
        event.widget.tag_add("sel","1.0","end")
        
    def gifFrame(self, frameG,frame):
        gButton = Button(frameG, text="Investigate",command=lambda:raise_frame(frame))
        gButton.pack()
        
def raise_frame(showFrame):
        showFrame.tkraise()
            

def faqPrint():
    #Providing training data to the classifier.
    scriptpath = os.path.dirname(__file__)
    filename_when = os.path.join(scriptpath,'when.txt')
    filename_where = os.path.join(scriptpath, 'where.txt')
    filename_who = os.path.join(scriptpath, 'who.txt')

    whenText = open(filename_when, 'r')
    whereText = open(filename_where, 'r')
    whoText = open(filename_who, 'r')
    if foo.entry.get() != '':
        c = Classifier(whenText,whereText,whoText,foo.text.get("1.0",END),foo.entry.get(),dict())
        foo.getValues(c)
    else:
        foo.getAlertValues()
    foo.entry.delete(0,END)
    
def faqEnterPrint(event):
    #Providing training data to the classifier.
    scriptpath = os.path.dirname(__file__)
    filename_when = os.path.join(scriptpath,'when.txt')
    filename_where = os.path.join(scriptpath, 'where.txt')
    filename_who = os.path.join(scriptpath, 'who.txt')

    whenText = open(filename_when, 'r')
    whereText = open(filename_where, 'r')
    whoText = open(filename_who, 'r')
    if foo.entry.get() != '':
        c = Classifier(whenText,whereText,whoText,foo.text.get("1.0",END),foo.entry.get(),dict())
        foo.getValues(c)
    else:
        foo.getAlertValues()
    foo.entry.delete(0,END)
    
root = Tk()
root.resizable(width=False, height=False)
foo = ScrollTxtArea(root)
    
    # print(a)
root.title('FAQCreator')
root.mainloop()

